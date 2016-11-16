<template>
  <div id="program-detail-view">
    <h3>Program Detail</h3>
    <info
      :name="program.name"
      :styles="program.styles"
    ></info>
  </div>
</template>

<script>
import {GET_VIEW} from '@store/modules/programs/types'
import Info from '@components/programs/Info.vue'

export default {
  name: 'program-detail-view',
  components: {
    Info
  },
  computed: {
    program () {
      return this.$store.state.programs.view
    },
    programId () {
      return this.$route.params.id
    }
  },
  methods: {
    loadProgram () {
      this.$store.dispatch(GET_VIEW, this.programId)
    }
  },
  watch: {
    'programId' (val, oldVal) {
      if (val !== oldVal) {
        this.loadProgram()
      }
    }
  },
  mounted () {
    this.loadProgram()
  }
}
</script>

<style scoped>
</style>
