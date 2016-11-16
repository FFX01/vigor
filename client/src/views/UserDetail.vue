<template>
  <div id="user-detail">
    <div class="user-info">
      <info :username="user.username"></info>
      <stats
        :height="user.height"
        :weight="user.weight"
      ></stats>
    </div>
  </div>
</template>

<script>
import Info from '@components/users/Info.vue'
import Stats from '@components/users/Stats.vue'

export default {
  name: 'user-detail',
  components: {
    Info,
    Stats
  },
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
