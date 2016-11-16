<template>
  <div id="info">
    <div class="name-wrapper">
      <h2 class="name-text">
        {{name}}
      </h2>
    </div>
    <div class="style-list-wrapper">
      <div class="style-wrapper"
        v-for="style in styles"
      >
        <h4 class="style-text">
          {{style}}
        </h4>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'info',
  props: [
    'name', 'styles'
  ]
}
</script>

<style scoped>
</style>
