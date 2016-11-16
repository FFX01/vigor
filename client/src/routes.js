import Vue from 'vue'
import VueRouter from 'vue-router'

import Home from '@views/Home.vue'
import UserList from '@views/UserList.vue'
import UserDetail from '@views/UserDetail.vue'
import ProgramList from '@views/ProgramList.vue'
import ProgramDetail from '@views/ProgramDetail.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '',
    name: 'home',
    component: Home
  },
  {
    path: '/users',
    name: 'user-list',
    component: UserList,
  },
  {
    path: '/users/:uid',
    name: 'user-detail',
    component: UserDetail
  },
  {
    path: '/programs',
    name: 'program-list',
    component: ProgramList
  },
  {
    path: '/programs/:id',
    name: 'program-detail',
    component: ProgramDetail
  }
]

const router = new VueRouter({
  routes
})

export default router
