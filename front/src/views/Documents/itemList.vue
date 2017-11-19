<template>
  <div class="item-list">
    <h3>{{ title }}</h3>
  </div>
</template>

<script>
export default {
  props: {
    title: {
      type: String,
      default: ''
    }
  }
}
</script>

<style  rel="stylesheet/scss" lang="scss" scoped>
.item-list {
  margin: 20px 0px;
  height: 100px;
  border: 1px solid black;
}
</style>
