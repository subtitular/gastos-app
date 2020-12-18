import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import Persona from '@/components/Persona'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
      path: '/persona/:idpersona',
      name: 'idpersona',
      component: Persona
    },
    {
      path: '/tipo_documento',
      name: 'tipo_documento',
      component: TipoDocumento
    }

  ]
})
