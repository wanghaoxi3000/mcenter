<template>
  <div class="app-container">
    <Row>
      <Col offset="4" span="14">

        <template v-for="(item, index) in blogItem" >
          <div class="blog-item" :class="index != 0 ? 'blog-item-li' : ''" :key="item.index">
            <document-item :itemInfo="item"></document-item>
          </div>
        </template>

        <Page class-name="blog-page" show-elevator :total="pageCount" :page-size="5"
              @on-change="getArticleList"></Page>

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
    getArticleList(page = 1) {
      articles(page).then(res => {
        this.blogItem = res.data.results.map((item) => {
          item.url = 'documents/' + item.url.split('/', 5).pop()
          return item
        })
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
