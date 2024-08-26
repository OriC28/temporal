#include<iostream>
using namespace std;

class Computador{
	public:
		string modelo;
		string ram;

	string propietario = "Miguel Diaz";

	void get_data(){
		cout<<"Modelo: "<<modelo<<"\n"<<"RAM: "<<ram;
	}
	private:

	void get_propietario(){
		cout<<"Propietario: "<<propietario<<"\n";
	}

};

class Telefono: public Computador{
public:
	int bateria;

	void bateria_mensaje(){
		if (bateria<20 && bateria>0){cout<<"La bateria se encuentra baja.\n";}
		else if (bateria == 100){
			cout<<"La bateria esta completamente cargada.\n";
		}
		else{
			cout<<"La bateria tiene carga aun...\n";
		}
	}
};


int main(){
	cout<<"--------------COMPUTADORA---------------"<<endl<<endl;
	Computador computador;
	computador.modelo = "Serie KDM38";
	computador.ram = "32GB";
	computador.get_data();

	cout<<"\n\n----------------TELEFONO---------------"<<endl<<endl;

	Telefono telefono;
	telefono.bateria = 6;
	telefono.modelo = "A53";
	telefono.ram = "16GB";
	telefono.bateria_mensaje();
	telefono.get_data();

	return 0;
}