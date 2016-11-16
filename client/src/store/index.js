import Vue from 'vue'
import Vuex from 'vuex'

import users from './modules/users'
import programs from './modules/programs'

Vue.use(Vuex)

const store = new Vuex.Store({
  modules: {
    users,
    programs
  }
})

export default store
