<template>
  <div class="app-container">

    <div class="blog-abstrac">
      <!-- <h1>Doc</h1> -->
      <document-item></document-item>
    </div>

  </div>
</template>

<script>
import { articles } from '../../api/documents'
import DocumentItem from './DocumentItem'

export default {
  components: {
    DocumentItem
  },
  created() {
    articles().then(res => console.log(res.data))
  }
}
</script>

<style rel="stylesheet/scss" lang="scss" scoped>
.blog-abstrac {
  text-align: center;
}
</style>
