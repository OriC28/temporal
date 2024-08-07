import conexion as conn
from model.movimientos import Transferencia
from datetime import datetime as dt

class TransferenciaData:
	def registrar(self, info: Transferencia):
		fecha = dt.now().strftime("%d/%m/%Y %H:%M:%S")
		self.db = conn.Conexion().conectar()
		self.cursor = self.db.cursor()
		resultado = self.cursor.execute("""INSERT INTO transferencias VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?)""",
										(info._monto, info._tipo, info._documento, info._internacional, info._dolares,
										fecha, False, info._motivo))
		self.db.commit()
		if self.cursor.rowcount == 1:
			return True
		return False