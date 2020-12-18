<template>
  <div id="Persona" class="persona">
    <h3>Nombres</h3>
    <input type="text" v-model="nombres.nombres" />
    <br />
    <h3>Apellidos</h3>
    <input type="text" v-model="nombres.apellidos" />
    <br />
    <h3>Fecha de Nacimiento</h3>
    <input type="date" v-model="fecha_nacimiento" />
    <h3>Nacionalidad</h3>
    <input type="text" v-model="nombres.nacionalidad" />
    <br />
    <br />
    <br />
    <button>Enviar</button>
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
        self.nombres = result.data[0];
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
