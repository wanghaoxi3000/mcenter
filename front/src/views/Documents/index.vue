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
        <item-list title="文章分类" :items="categories" @select="categorySelect" :active="curCategory"></item-list>
        <item-list title="文章归档" :items="archives" @select="archiveSelect" :active="curArchive"></item-list>
      </Col>
    </Row>
    </keep-alive>
  </div>
</template>

<script>
import { articles, categories, archives } from '../../api/documents'
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
      archiveList: [],
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
    },
    archives() {
      let archive = []
      for (const item of this.archiveList) {
        archive.push(item.name)
      }
      return archive
    },
    curCategory() {
      for (const item of this.categoryList) {
        if (item.slug === this.$route.query.category) { return item.name }
      }
    },
    curArchive() {
      for (const item of this.archiveList) {
        if (item.slug === this.$route.query.archive) { return item.name }
      }
    }
  },
  created() {
    this.getArticleList(this.$route.params.page, this.$route.query.category, this.$route.query.archive)
    this.getCategoryList()
    this.getArchivesList()
  },
  methods: {
    getArticleList(page = 1) {
      articles(page, this.$route.query.category, this.$route.query.archive).then(res => {
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

    async getArchivesList() {
      const { data } = await archives()
      this.archiveList = data.map((val => {
        const time = val.record.split('-')
        return {
          name: `${time[0]}年${time[1]}日 (${val.num})`,
          slug: `${time[0]}${time[1]}`
        }
      }))
    },

    categorySelect(index) {
      this.categoryIndex = index
      this.$router.push({ name: 'blog', query: { category: this.categoryList[index].slug }})
    },

    archiveSelect(index) {
      this.archiveIndex = index
      this.$router.push({ name: 'blog', query: { archive: this.archiveList[index].slug }})
    },

    pageChange(val) {
      this.$router.push({ path: `/documents/page/${val}/`, query: this.$route.query })
    }
  },

  beforeRouteUpdate(to, from, next) {
    next()
    this.getArticleList(to.params.page)
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
