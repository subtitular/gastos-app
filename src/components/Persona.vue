<template>
  <div>
    <b-container v-if="resultadoOK">
      <b-jumbotron class="text-center">
        <template #header>Información Personal</template>
      </b-jumbotron>
      <b-form>
        <b-col md="12">
          <b-form-group id="grupo-1" label="Nombres:" description="">
            <b-form-input id="nombres" v-model="persona.nombres" type="text">
            </b-form-input>
          </b-form-group>
          <b-form-group id="grupo-2" label="Apellidos:" description="">
            <b-form-input
              id="apellidos"
              v-model="persona.apellidos"
              type="text"
            >
            </b-form-input>
          </b-form-group>
          <b-form-group
            id="grupo-3"
            label="Fecha de Nacimiento:"
            description=""
          >
            <b-form-input v-if="persona"
              id="fecha_nacimiento"
              v-model="persona.fecha_nacimiento"
              type="date"
            >
            </b-form-input>
          </b-form-group>
          <b-form-group id="grupo-4" label="Nacionalidad:" description="">
            <b-form-input
              id="nacionalidad"
              v-model="persona.nacionalidad"
              type="text"
            >
            </b-form-input>
          </b-form-group>
          <!-- <b-form-group v-if="persona.documento.tipo_documento.id !== 1" id="grupo-5" label="Documento:" description="">-->
            <Documento :doc="persona.documento"></Documento>
            <!-- <b-form-input  v-if="persona.documento.tipo_documento.id !== 0"
              id="Documento"
              v-model="persona.documento.id"
              type="text"
            >
            </b-form-input> -->
          <!-- </b-form-group>-->
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
//import Documento from './Documento.vue';
//import Documento from './Documento.vue';

export default {
  name: "Persona",
  components: {
    Documento
  },
  data: function () {
    return {

      persona: {},
      resultadoOK: false,
      
      /*
      
        id: 0,
        nombres: "",
        apellidos: "",
        fecha_nacimiento: moment(new Date()).format("YYYY-MM-DD"),
        nacionalidad: "",
        documento: null,

      */

    };
  },
  created: function () {
    this.idpersona = this.$route.params.idpersona; 
    let self = this;
    
    axios
      .get("http://127.0.0.1:8000/persona/"+ self.idpersona)
      .then((result) => {
        self.persona = result.data;
        self.resultadoOK = true
        console.log(self.persona)


          self.persona.fecha_nacimiento = moment(self.persona.fecha_nacimiento).format(
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
