import Vue from 'vue'
import VueRouter from 'vue-router'

import Home from '@views/Home.vue'
import UserList from '@views/UserList.vue'
import UserProfile from '@views/UserProfile.vue'

Vue.use(VueRouter)

const routes = [
  {path: '', component: Home},
  {
    path: '/users/',
    name: 'user-list',
    component: UserList
  },
  {
    path: '/users/:uid/',
    name: 'user-profile',
    component: UserProfile
  }
]

const router = new VueRouter({
  routes
})

export default router
