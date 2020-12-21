<template>
<div> 
    <div class="main-component">
      <router-view></router-view>
    </div>
</div>

</template>

<script>
import axios from'axios';
import Documento from './components/Documento';
//import Home from './components/Home';

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
