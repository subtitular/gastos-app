<template>
  <div>
    <b-container>
      <b-jumbotron class="text-center">
        <template #header>Datos del tercero</template>
      </b-jumbotron>
      <b-form>
        <b-col md="12">
          <b-form-group id="grupo-1" label="Nombres:" description="">
            <b-form-input id="nombres" v-model="nombres.nombres" type="text">
            </b-form-input>
          </b-form-group>
          <b-form-group id="grupo-2" label="Apellidos:" description="">
            <b-form-input
              id="apellidos"
              v-model="nombres.apellidos"
              type="text"
            >
            </b-form-input>
          </b-form-group>
          <b-form-group
            id="grupo-3"
            label="Fecha de Nacimiento:"
            description=""
          >
            <b-form-input
              id="fecha_nacimiento"
              v-model="fecha_nacimiento"
              type="date"
            >
            </b-form-input>
          </b-form-group>
          <b-form-group id="grupo-4" label="Nacionalidad:" description="">
            <b-form-input
              id="nacionalidad"
              v-model="nombres.nacionalidad"
              type="text"
            >
            </b-form-input>
          </b-form-group>
          </b-form-group>
          <b-form-group id="grupo-5" label="Saldo:" description="">
            <b-form-input
              id="saldo"
              v-model="nombres.saldo"
              type="number"
            >
            </b-form-input>
          </b-form-group>
          <b-button type="submit" variant="primary">Enviar</b-button>
        </b-col>
      </b-form>
    </b-container>
  </div>
</template>

<script>
import axios from "axios";
import moment from "moment";
import Documento from "./Documento";

export default {
  name: "Persona",
  components: {
    Documento,
  },
  data: function () {
    return {
      idpersona: 0,
      nombres: "",
      fecha_nacimiento: "",
    };
  },

  created: function () {
    this.idpersona = this.$route.params.idpersona;

    let self = this;
    axios
      .get("http://127.0.0.1:8000/persona/" + self.idpersona)
      .then((result) => {
        self.nombres = result.data;
        self.fecha_nacimiento = moment(self.nombres.fecha_nacimiento).format(
          "YYYY-MM-DD"
        );
      })
      .catch((error) => {
        alert(error);
      });
  },
};
</script>

<style>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
