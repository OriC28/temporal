from model.movimientos import DepositoInternacional
import conexion as conn
from datetime import datetime as dt

class DepositoData:
	def registrar(self, info: DepositoInternacional):
		fecha = dt.now().strftime("%d/%m/%Y %H:%M:%S")
		self.db = conn.Conexion().conectar()
		self.cursor = self.db.cursor()
		resultado = self.cursor.execute("""INSERT INTO depositos VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?,
										 ?, ?, ?, ?, ?, ?, ?)""",
		(info._tipo, info._documento, info._primer_nombre, info._segundo_nombre, info._primer_apellido,
			info._segundo_apellido, info._sexo, info._fecha_nacimiento, info._lugar_nacimiento,
			info._motivo, info._monto, info._internacional, info._dolares, info._terminos, fecha))
		self.db.commit()
		if self.cursor.rowcount == 1:
			return True
		return False