
class Transferencia:
	def __init__(self, tipo: str, documento: str, motivo: str,
				monto: int, dolares: bool, internacional: bool):
		self._tipo = tipo
		self._documento = documento
		self._motivo = motivo
		self._monto = monto
		self._dolares = dolares
		self._internacional = internacional

class DepositoInternacional:
	def __init__(self, tipo: str, documento: str, motivo: str, monto: int, primer_nombre: str,
				segundo_nombre: str, primer_apellido: str, segundo_apellido: str, sexo: str,
				fecha_nacimiento: str, lugar_nacimiento: str, dolares: bool, internacional: bool,
				terminos: bool):
		self._tipo = tipo
		self._documento = documento
		self._motivo = motivo
		self._monto = monto
		self._primer_nombre = primer_nombre
		self._segundo_nombre = segundo_nombre
		self._primer_apellido = primer_apellido
		self._segundo_apellido = segundo_apellido
		self._sexo = sexo
		self._fecha_nacimiento = fecha_nacimiento
		self._lugar_nacimiento = lugar_nacimiento
		self._internacional = internacional
		self._dolares = dolares 
		self._terminos = terminos 