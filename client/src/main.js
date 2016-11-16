import Vue from 'vue'
import VueResource from 'vue-resource'

import router from './routes'
import App from './App.vue'
import store from './store'

Vue.use(VueResource)

const http = new VueResource({})

new Vue({
  router,
  http,
  store,
  el: '#app',
  render: h => h(App)
})
