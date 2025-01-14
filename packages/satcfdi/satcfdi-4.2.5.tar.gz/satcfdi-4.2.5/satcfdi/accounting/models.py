from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal
from uuid import UUID


from ..create.catalogos import EstadoComprobante
from ..create.cfd.catalogos import MetodoPago, TipoDeComprobante, TipoRelacion
from ..create.compute import make_impuestos_dr_parcial, rounder, group_impuestos, encode_impuesto, calculate_partial
from ..xelement import XElement
from ..cfdi import CFDI


class SatCFDI(CFDI):
    """
    SatCFDI is an extension of a CFDI to represent a CFDI that has been sent to SAT
    """

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls, *args, **kwargs)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.relations = []  # type: list[Relation]
        self.payments = []  # type: list[Payment]

    @property
    def uuid(self):
        return UUID(self["Complemento"]["TimbreFiscalDigital"]["UUID"])

    @property
    def name(self):
        return self.get("Serie", "") + self.get("Folio", "")

    @property
    def saldo_pendiente(self) -> Decimal | None:
        if self["TipoDeComprobante"] == TipoDeComprobante.INGRESO:
            # Nota de crédito de los documentos relacionados
            credit_notes = sum(
                c.comprobante["Total"]
                for c in self.relations
                if c.cfdi_relacionados["TipoRelacion"] == TipoRelacion.NOTA_DE_CREDITO_DE_LOS_DOCUMENTOS_RELACIONADOS
                and c.comprobante['TipoDeComprobante'] == TipoDeComprobante.EGRESO
                and c.comprobante.estatus == EstadoComprobante.VIGENTE
            )
            insoluto = min(
                (c.docto_relacionado['ImpSaldoInsoluto']
                 for c in self.payments
                 if c.comprobante.estatus == EstadoComprobante.VIGENTE),
                default=None
            )
            if insoluto is not None:
                return insoluto - credit_notes

            insoluto = self["Total"] - credit_notes
            if self["MetodoPago"] == MetodoPago.PAGO_EN_PARCIALIDADES_O_DIFERIDO:
                return insoluto
            if self["MetodoPago"] == MetodoPago.PAGO_EN_UNA_SOLA_EXHIBICION:
                return Decimal(0)

        return None

    @property
    def ultima_num_parcialidad(self) -> int:
        return max((c.docto_relacionado['NumParcialidad'] for c in self.payments), default=0)

    def consulta_estado(self) -> dict:
        raise NotImplementedError()

    @property
    def estatus(self) -> EstadoComprobante:
        raise NotImplementedError()

    @property
    def fecha_cancelacion(self) -> datetime | None:
        raise NotImplementedError()


@dataclass(slots=True, init=True)
class Relation:
    cfdi_relacionados: XElement
    comprobante: SatCFDI


@dataclass(slots=True, init=True)
class Payment:
    comprobante: SatCFDI
    pago: XElement = None
    docto_relacionado: XElement = None


@dataclass
class PaymentsDetails(Payment):
    comprobante_pagado: SatCFDI = None

    def __post_init__(self):
        if self.pago:
            self.impuestos = self.docto_relacionado.get('ImpuestosDR')
            if self.impuestos is None:
                self.impuestos = make_impuestos_dr_parcial(
                    conceptos=self.comprobante_pagado['Conceptos'],
                    imp_saldo_ant=self.docto_relacionado['ImpSaldoAnt'],
                    imp_pagado=self.docto_relacionado['ImpPagado'],
                    total=self.comprobante_pagado['Total'],
                    rnd_fn=rounder(self.comprobante_pagado['Moneda'])
                )

            self.impuestos = group_impuestos([{
                "ImpuestosDR": self.impuestos
            }], pfx="DR", ofx="")

            for imp, imps in self.impuestos.items():
                self.impuestos[imp] = {
                    encode_impuesto(
                        impuesto=v['Impuesto'],
                        tipo_factor=v.get("TipoFactor"),
                        tasa_cuota=v.get('TasaOCuota')
                    ): v
                    for v in imps
                }

            def calc_parcial(field):
                return calculate_partial(
                    value=self.comprobante_pagado.get(field),
                    imp_saldo_ant=self.docto_relacionado['ImpSaldoAnt'],
                    imp_pagado=self.docto_relacionado["ImpPagado"],
                    total=self.comprobante_pagado["Total"],
                    rnd_fn=rounder(self.comprobante_pagado['Moneda'])
                )

            self.sub_total = calc_parcial("SubTotal")
            self.descuento = calc_parcial("Descuento")
            self.total = self.docto_relacionado["ImpPagado"]

        else:
            self.impuestos = self.comprobante.get("Impuestos", {})
            self.sub_total = self.comprobante["SubTotal"]
            self.descuento = self.comprobante.get("Descuento")
            self.total = self.comprobante["Total"]
