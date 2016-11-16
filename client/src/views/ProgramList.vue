<template>
  <div id="program-list-view">
    <h2>Programs</h2>
    <div class="list">
      <div class="program-wrapper"
        v-for="program in programs"
      >
        <router-link :to="{name: 'program-detail', params: {id: program.id}}">
          {{program.name}}
        </router-link>
      </div>
    </div>
  </div>
</template>

<script>
import {GET_LIST} from '@store/modules/programs/types'

export default {
  name: 'program-list-view',
  computed: {
    programs () {
      return this.$store.state.programs.list
    }
  },
  methods: {
    loadPrograms () {
      this.$store.dispatch(GET_LIST)
    }
  },
  mounted () {
    this.loadPrograms()
  }
}
</script>

<style scoped>
</style>
