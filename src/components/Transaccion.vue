<template>
  <div>
    <b-container>
      <b-card
        name="cabecera"
        img-src="https://i.ibb.co/njFyFmD/byrsapp-logo.png"
        img-alt="byrsapp_logo"
        img-left
        img-height="100"
        img-width="100"
        class="mb-3"
      >
        <b-card-title 
          class="text-center"
          name="titulo_cabecera"
        >
          <h1>Captura de movimientos</h1>
        </b-card-title>
      </b-card>

      <b-form @submit="grabaTransaccion" @reset="onReset" v-if="show">
        <b-form-group
          id="desId"
          label="Id:"
          label-for="desID"
          description="Indicador de la transaccion"
        >
          <b-form-input
            id="id"
            v-model="form.id"
            type="number"
            placeholder="Ingrese el ID de la transaccion"
            required
          >
          </b-form-input>
        </b-form-group>

        <b-form-group
          id="desCapturaValor"
          label="Valor:"
          label-for="desCapturaValor"
          description="Ingrese el valor de la transaccion"
        >
          <b-form-input
            id="valor"
            v-model="form.valor"
            type="number"
            placeholder="Ingrese un valor"
            required
          >
          </b-form-input>
        </b-form-group>

        <b-form-group
          id="desCapturaTipo"
          label="Tipo de movimiento:"
          label-for="desCapturaTipo"
        >
          <b-form-select
            id="tipo"
            v-model="form.tipo"
            :options="tipos"
            required
          >
          </b-form-select>
        </b-form-group>

        <b-form-group
          id="capturaFecha"
          label="Fecha de la transaccion:"
          label-for="capturaFecha"
        >
          <b-form-datepicker
            id="fecha"
            v-model="form.fecha"
            class="mb-2"
            placeholder="Ingrese fecha de la transaccion"
          >
          </b-form-datepicker>
        </b-form-group>
        <b-form-group
          id="desCapturaDetalle"
          label="Detalle del movimiento:"
          label-for="desCapturaDetalle"
          description="Ingrese el detalle de la transaccion"
        >
          <b-form-input
            id="detalle"
            v-model="form.detalle"
            type="text"
            placeholder="Ingrese el detalle correspondiente al movimiento"
            required
          >
          </b-form-input>
        </b-form-group>
        <br/>

        <b-button type="submit" variant="primary">Agregar</b-button>
        <b-button variant="outline-success" href="/transaccion/consulta">Ver transacciones</b-button>
        <b-button class="mx-5" type="reset" variant="danger">Limpiar</b-button>
      </b-form>
    </b-container>
  </div>
</template>

<script>

import axios from 'axios';

export default {
  data() {
    return {
      form: {
        id: '',
        valor: '',
        tipo: null,
        fecha: new Date().toISOString(),
        detalle: ''
      },
      tipos: [{ text: "Seleccione el tipo de movimiento", value: null }, "Ingreso", "Gasto"],
      show: true
    };
  },

  methods: {
    grabaTransaccion: function(){
        var self = this
        axios.post("http://127.0.0.1:8000/transaccion/", JSON.stringify(self.form),  {headers: {}})
            .then((result) => {
                alert("La transaccion se agrego correctamente");

            })
            .catch((error) => {
                  alert("ERROR " + error + "Comuniquese con el area encargada");
            });
    },



    onReset(event) {
      event.preventDefault();
      // Reset our form values
      this.form.id = '';
      this.form.valor = '';
      this.form.tipo = null;
      this.form.fecha = "";
      this.form.detalle = "";

      this.form.checked = [];
      // Trick to reset/clear native browser form validation state
      this.show = false;
      this.$nextTick(() => {
        this.show = true;
      });
    }
  }
};
</script>
