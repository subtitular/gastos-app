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
import Documento from './Documento';

export default {
  name: 'Persona',
  components:{
    Documento
  },
  data: function(){
    return { idpersona:0
    }
  }
  ,
  created: function(){
            console.log(idpersona)
            this.idpersona = this.$route.params.idpersona
        },
  created: function(){
    let self = this
    console.log(idpersona)
    axios.get("http://127.0.0.1:8000/persona/{idpersona}")
      .then((result) => {  
        self.tipo_documentos = result.data
        console.log(result.data)
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
