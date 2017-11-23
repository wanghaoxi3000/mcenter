<template>
  <div class="app-container">
    <keep-alive>
    <Row>
      <Col :xs="{offset: 1, span: 22}"
        :sm="{offset: 3, span: 14}">

        <template v-for="(item, index) in blogItem" >
          <div class="blog-item" :class="index != 0 ? 'blog-item-li' : ''" :key="item.index">
            <document-item :itemInfo="item"></document-item>
          </div>
        </template>

        <Page class-name="blog-page" show-elevator :total="blogCount" :page-size="5" :current="currentPage"
              @on-change="pageChange"></Page>

      </Col>

      <Col :xs="{offset: 1, span: 22}"
        :sm="{offset:1, span:4}">
        <item-list title="文章分类" :items="categories" @select="categorySelect"></item-list>
      </Col>
    </Row>
    </keep-alive>
  </div>
</template>

<script>
import { articles, categories } from '../../api/documents'
import DocumentItem from './DocumentItem'
import itemList from './itemList'

export default {
  components: {
    DocumentItem,
    itemList
  },
  data() {
    return {
      blogItem: {},
      categoryList: [],
      blogCount: 0,
      currentPage: 1
    }
  },
  computed: {
    categories() {
      let cate = []
      for (const item of this.categoryList) {
        cate.push(item.name)
      }
      return cate
    }
  },
  created() {
    this.getArticleList(this.$route.params.page, this.$route.query.category)
    this.getCategoryList()
  },
  methods: {
    getArticleList(page = 1, category) {
      articles(page, category).then(res => {
        this.blogItem = res.data.results
        this.blogCount = res.data.count
        this.currentPage = Number(page)
      })
    },

    async getCategoryList() {
      const { data } = await categories()
      this.categoryList = data.map((val) => {
        val.name = `${val.name} (${val.count})`
        return val
      })
    },

    categorySelect(index) {
      this.$router.push({ name: 'blog', query: { category: this.categoryList[index].slug }})
    },

    pageChange(val) {
      this.$router.push({ path: `/documents/page/${val}/` })
    }
  },
  beforeRouteUpdate(to, from, next) {
    this.getArticleList(to.params.page, to.query.category)
    next()
  },
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
.blog-page {
  text-align: center;
  margin-top: 15px;
}
</style>
