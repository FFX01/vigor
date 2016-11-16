<template>
  <div id="user-list-view">
    <h2>User List</h2>
    <div class="user-list-wrapper">
      <div class="user-wrapper"
        v-for="user in users"
      >
        <div class="username-wrapper">
          <h3 class="username-text">
            <router-link :to="{name: 'user-profile', params: {uid: user.id}}">
              {{user.username}}
            </router-link>
          </h3>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'user-detail-vue',
  data () {
    return {
      users: []
    }
  },
  created () {
    const url = '/api/users/'
    this.$http.get(url).then((response) => {
      return response.json()
    }).then((data) => {
      this.users = data.objects
    })
  },
  methods: {
    buildUrl (uid) {
      return `/users/${uid}/profile/`
    }
  }
}
</script>
