import { Component } from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import './App.css';

class App extends Component {
  constructor(props) {
    super(props)
    this.state = {
      articulos:[{
        codigo:1,
        descripcion:'coca-cola',
        precio:2.50
      },{
        codigo:2,
        descripcion:'inka-cola',
        precio:2.20
      },{
        codigo:3,
        descripcion:'fanta',
        precio:1.70
      }]
    }
    this.borrar = this.borrar.bind(this);
  }
  
  borrar = (cod) => {
    var temp = this.state.articulos.filter((el) => el.codigo !== cod);
    this.setState({
      articulos: temp
    });
  }
  
  render() {
    return (
      <div className="container mt-4">
        <table className="table">
          <thead className="thead-dark">
            <tr>
              <th scope="col">Codigo</th>
              <th scope="col">Descripción</th>
              <th scope="col">Precio</th>
              <th scope="col">Borrar</th>
            </tr>
          </thead>
          <tbody>
            {this.state.articulos.map(elemento => {
              return (
                <tr key={elemento.codigo}>
                  <td>{elemento.codigo}</td>
                  <td>{elemento.descripcion}</td>
                  <td>{elemento.precio}</td>
                  <td>
                    <button 
                      className="btn btn-danger" 
                      onClick={() => this.borrar(elemento.codigo)}
                    >
                      Borrar
                    </button>
                  </td>
                </tr>
              )
            })}
          </tbody>
        </table>
      </div>
    );
  }
}

export default App;
