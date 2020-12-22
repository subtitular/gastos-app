<template>
  <b-container>
    <b-card
      name="cabecera"
      img-src="https://i.ibb.co/njFyFmD/byrsapp-logo.png"
      img-alt="byrsapp_logo"
      img-left
      img-height="100"
      img-width="100"
      class="mb-3"
    >
      <b-card-title class="text-center" name="titulo_cabecera">
        <h1>Lista de movimientos</h1>
      </b-card-title>
    </b-card>
    <div class="container-fluid d-flex justify-content-center">
        <table class="table col-sm-4">
          <thead>
            <tr>
              <td scope="row" class="fondo">ID</td>
          <td>Detalle</td>
          <th>Valor</th>
        </tr>
      </thead>
      <tbody v-for="item in items">
        <tr>
          <td scope="row" class="fondo">{{ item.id }}</td>
          <td>{{ item.detalle }}</td>
          <th>{{ item.valor }}</th>
        </tr>
        <td class="total">{{ suma }}</td>
      </tbody>
    </table>
    </div>
    <b-button variant="outline-success" href="/transaccion"
      >Capturar transacciones</b-button
    >
  </b-container>
</template>

<script>
import axios from "axios";

export default {
    name: "TablaTransacciones",

    data() {
    return {
      items: []
    };
  },


  created: function() {
    let self = this;
    axios
      .get("https://byrsapp.herokuapp.com/transaccion/consulta/")
      .then(result => {
        self.items = result.data;
        /*            self.fecha_nacimiento = moment(self.nombres.fecha_nacimiento).format(
            "YYYY-MM-DD" 
            ); */
      })
      .catch(error => {
        alert(error);
      });
  },

};
</script>
