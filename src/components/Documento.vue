<template>
<div> 
  <tipo-documento></tipo-documento><input type="text" placeholder="Numero"/>
</div>

</template>

<script>
import axios from'axios';
import TipoDocumento from './TipoDocumento';

export default {
  name: 'Documento',
  components:{
    TipoDocumento
  },
  data: function(){
    return { tipo_documentos:[]
    }
  },
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
