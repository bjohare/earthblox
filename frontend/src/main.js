import Vue from 'vue'
import VeeValidate from "vee-validate";
import store from '@/store/index'
import router from '@/routes/index'

import { BootstrapVue, BootstrapVueIcons } from "bootstrap-vue";
import "bootstrap/dist/css/bootstrap.css";
import "bootstrap-vue/dist/bootstrap-vue.css";

import axios from 'axios'
axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'

import App from '@/App.vue'
import './registerServiceWorker'

Vue.config.productionTip = false

Vue.use(BootstrapVue);
Vue.use(BootstrapVueIcons);
Vue.use(VeeValidate, {
  inject: true,
  fieldsBagName: "veeFields",
  classes: true,
  classNames: {
    valid: "is-valid",
    invalid: "is-invalid"
  }
});

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
