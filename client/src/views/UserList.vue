<template>
  <div id="user-list-view">
    <h2>User List</h2>
    <div class="user-list-wrapper">
      <div class="user-wrapper"
        v-for="user in users"
      >
        <div class="username-wrapper">
          <h3 class="username-text">
            <router-link :to="{name: 'user-detail', params: {uid: user.id}}">
              {{user.username}}
            </router-link>
          </h3>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import {GET_LIST} from '@store/modules/users/types'

export default {
  name: 'user-list-view',
  computed: {
    users () {
      return this.$store.state.users.list
    }
  },
  methods: {
    loadUsers () {
      this.$store.dispatch(GET_LIST)
    }
  },
  mounted () {
    this.loadUsers()
  }
}
</script>
