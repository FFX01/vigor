import Vue from 'vue'

import * as types from './types'

const state = {
  view: {},
  edit: {},
  list: []
}

const actions = {
  [types.GET_VIEW] ({commit}, uid) {
    let url = `/api/users/${uid}/`
    Vue.http.get(url).then(response => {
      return response.json()
    }).then(data => {
      commit(types.SET_VIEW, data)
    }).catch(error => {
      console.error(error)
    })
  },
  [types.GET_EDIT] ({commit}, uid) {
    let url = `/api/users/${uid}/`
    Vue.http.get(url).then(response => {
      return response.json()
    }).then(data => {
      commit(types.SET_EDIT, data)
    }).catch(error => {
      console.error(error)
    })
  },
  [types.GET_LIST] ({commit}) {
    let url = '/api/users/'
    Vue.http.get(url).then(response => {
      return response.json()
    }).then(data => {
      commit(types.SET_LIST, data.objects)
    }).catch(error => {
      console.error(error)
    })
  }
}

const mutations = {
  [types.SET_VIEW] (state, user) {
    state.view = user
  },
  [types.SET_EDIT] (state, user) {
    state.edit = user
  },
  [types.SET_LIST] (state, users) {
    state.list = users
  }
}

const users = {
  state,
  mutations,
  actions
}

export default users
