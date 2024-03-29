import Vue from 'vue'
import App from './App.vue'
import router from './router'
import vuetify from './plugins/vuetify'
import Axios from 'axios';
import VueAxios from 'vue-axios';
import DatetimePicker from 'vuetify-datetime-picker';
import VueApexCharts from 'vue-apexcharts'


Vue.config.productionTip = false

Vue.use(VueAxios, Axios, DatetimePicker,VueApexCharts);

Vue.prototype.$axios = Axios;

Vue.axios.defaults.baseURL = `http://192.168.0.108:8181`;

new Vue({
  router,
  vuetify,
  render: h => h(App)
}).$mount('#app')
