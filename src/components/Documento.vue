<template>
<div> 
  
  
  <b-container v-if="doc != null">
    <b-col md="12">
      {{ doc.codigo }}
      <!--
      <tipo-documento></tipo-documento>
      <b-form-input type="text" placeholder="Numero"></b-form-input>
      <b-form-input type="date" v-if="documento.tipo_documento.vence == true" v-model="documento.fecha_vigencia"></b-form-input>
-->

    </b-col>
    
  </b-container>

  
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
  props:{
     doc: {}
  },
   
  
  data: function(){
    return { 
      tipo_documentos:[],
      documento: {
        id: 0,
        nombre: "",
        abreviatura: "",
        vence: false
      }
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
