import Router from 'vue-router'
import Persona from '@/components/Persona'
import Transaccion from '@/components/Transaccion'
import TransacionConsulta from '@/components/TablaTransacciones'
import App from './App'

export default new Router({
  mode: 'history',
  base: __dirname,
  routes: [
    {
      path: '/',
      name: 'transaccion',
      component: Transaccion
    },
    {
      path: '/persona/:idpersona',
      name: 'idpersona',
      component: Persona
    },
    {
      path: '/transaccion',
      name: 'transaccion',
      component: Transaccion
    },
    {
      path: '/transaccion/consulta',
      name: 'trasaccion_consulta',
      component: TransacionConsulta
    }

  ]
})
