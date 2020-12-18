<template>
<div> 
  <h3>Nombres</h3><input type="text"/><br>
  <h3>Apellidos</h3><input type="text"/><br>
  <h3>Fecha de Nacimiento</h3><input type="date" id="start" name="trip-start"
       value="2005-06-30"
       min="1900-01-01" >
  <h3>Nacionalidad</h3><input type="text"/><br>
  <documento></documento>
  <button>Enviar</button>
</div>

</template>

<script>
import axios from'axios';
import Documento from './components/Documento';

export default {
  name: 'App',
  components:{
    Documento
  },
  /*data: function(){
    return { documento:[]
    }
  },*/
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
