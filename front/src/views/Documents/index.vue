<template>
  <div class="app-container">
    <Row>
      <Col offset="4" span="14">
        <template v-for="(item, index) in blogItem" >
          <div class="blog-item" :class="index != 0 ? 'blog-item-li' : ''" :key="item.id">
            <document-item :itemInfo="item"></document-item>
          </div>
        </template>

        <Page :total="pageCount" :page-size="5" show-elevator class-name="blog-page"></Page>
      </Col>

      <Col span="4">

      </Col>
    </Row>
  </div>
</template>

<script>
import { articles } from '../../api/documents'
import DocumentItem from './DocumentItem'

export default {
  components: {
    DocumentItem
  },
  data() {
    return {
      blogItem: {},
      pageCount: 0
    }
  },
  created() {
    this.getArticleList()
  },
  methods: {
    getArticleList() {
      articles().then(res => {
        console.log(res.data)
        this.blogItem = res.data.results
        this.pageCount = res.data.count
      })
    }
  }
}
</script>

<style rel="stylesheet/scss" lang="scss" scoped>
.blog-item {
  padding-bottom: 25px;

  &-li {
    border-top: 2px solid #e9eaec;
    padding-top: 25px;
  }
}
.blog-page{
  text-align: center;
  margin-top: 15px;
}
</style>
