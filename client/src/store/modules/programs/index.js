import Vue from 'vue'

import * as types from './types'

const state = {
  view: {},
  edit: {},
  list: []
}

const actions = {
  [types.GET_LIST] ({commit}) {
    let url = '/api/programs/'
    Vue.http.get(url).then(response => {
      return response.json()
    }).then(data => {
      commit(types.SET_LIST, data.objects)
    }).catch(err => {
      console.error(err)
    })
  },
  [types.GET_VIEW] ({commit}, id) {
    let url = `/api/programs/${id}/`
    Vue.http.get(url).then(response => {
      return response.json()
    }).then(data => {
      commit(types.SET_VIEW, data)
    }).catch(err => {
      console.error(err)
    })
  },
  [types.GET_EDIT] ({commit}, id) {
    let url = `/api/programs/${id}/`
    Vue.http.get(url).then(response => {
      return response.json()
    }).then(data => {
      commit(types.SET_EDIT, data)
    }).catch(err => {
      console.error(err)
    })
  }
}

const mutations = {
  [types.SET_LIST] (state, objects) {
    state.list = objects
  },
  [types.SET_VIEW] (state, object) {
    state.view = object
  },
  [types.SET_EDIT] (state, object) {
    state.edit = object
  }
}

const programs = {
  state,
  mutations,
  actions
}

export default programs
