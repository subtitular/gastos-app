<template>
  <div> 
    <h3>Tipo de documento</h3>
    <select name="tipo_documento" id="tipo_documento">
      <option v-for="(value,index) in tipo_documentos" v-bind:key="index">{{value.nombre}}</option>
    </select>
  </div>
</template>

<script>
import axios from'axios';
export default {
  name: 'tipo-documento',
  data: function(){
    return { tipo_documentos:[]
    }
  },
  created: function(){
    let self = this
    axios.get("http://127.0.0.1:8000/tipo_documento")
      .then((result) => {  
        self.tipo_documentos = result.data
      }).catch((error) => { alert(error)});
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
