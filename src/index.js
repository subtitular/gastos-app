import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import Persona from '@/components/Persona'
import TipoDocumento from '@/components/TipoDocumento'
import Home from '@/components/Home'
import App from './App'

export default new Router({
  mode: 'history',
  base: __dirname,
  routes: [
    {
      path: '/',
      name: "root",
      component: App
    },
    {
      path: '/hello',
      name: "helloword",
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
    },
    {
      path: '/home',
      name: 'home',
      component: Home
    }

  ]
})
