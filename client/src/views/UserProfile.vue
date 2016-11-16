<template>
  <div id="user-profile">
    <div class="info-wrapper">
      <div class="username-wrapper">
        <h3 class="username-text">
          {{user.username}}
        </h3>
      </div>
      <div class="stats-wrapper">
        <span class="weight-text">
          Weight: {{user.weight}}
        </span>
        <span class="height-wrapper">
          Height: {{user.height}}
        </span>
      </div>
      <div class="meta-wrapper">
        <span class="date-joined-wrapper">
          Date Joined: {{user.date_joined}}
        </span>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'user-profile',
  computed: {
    user () {
      return this.$store.state.users.view
    },
    uid () {
      return this.$route.params.uid
    }
  },
  watch: {
    'uid' (val, oldVal) {
      if (val !== oldVal) {
        this.loadUser()
      }
    }
  },
  methods: {
    loadUser () {
      this.$store.dispatch('users.GET_VIEW', this.uid)
    }
  },
  mounted () {
    this.loadUser()
  }
}
</script>
