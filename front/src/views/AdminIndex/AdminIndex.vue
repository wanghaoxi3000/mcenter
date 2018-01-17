<template>
  <div>
    <div class="admin-index-top-btn">
      <Button type="primary">发布文章</Button>
      <Button type="error" :disabled="!selectItem">删除所选</Button>
    </div>

    <TableArticle
      :columnsList="blogTable"
      :value="tableData"
      :valueNum="valueCount"
      :loading="loading"
      @page-change="handlePageChange">
    </TableArticle>
  </div>
</template>

<script>
import { articles } from '../../api/documents'
import TableArticle from './components/TableArticle'

export default {
  components: {
    TableArticle
  },
  data() {
    return {
      loading: false,     // 表格等待标致
      tableData: [],      // 表格数据
      valueCount: 0,      // 数据总数
      selectItem: false,  // 是否处于选中状态
      pageLimit: 10,      // 每页显示条数
      pageNum: 1,         // 当前页
      blogTable: [        // 表格列数据
        {
          type: 'selection',
          width: 60,
          align: 'center'
        },
        {
          type: 'index',
          align: 'center',
          title: '序号',
          width: 70
        },
        {
          title: '标题',
          key: 'title',
          ellipsis: true
        },
        {
          title: '来源',
          align: 'center',
          key: 'own',
          width: 100
        },
        {
          title: '类别',
          align: 'center',
          key: 'category',
          width: 160
        },
        {
          title: '时间戳',
          align: 'center',
          key: 'timestamp',
          width: 140
        },
        {
          title: '阅读次数',
          align: 'center',
          key: 'readNum',
          width: 100
        },
        {
          title: '操作',
          align: 'center',
          width: 120,
          key: 'handle',
          handle: ['delete']
        }
      ]
    }
  },
  created() {
    this.fetchData()
  },
  methods: {
    // 获取博客列表数据
    async fetchData() {
      this.loading = true
      let offset = (this.pageNum - 1) * this.pageLimit
      const { data } = await articles(this.pageLimit, offset)
      this.valueCount = data.count
      this.tableData = data.results.map(item => {
        if (item.hasOwnProperty('own')) {
          item.own = item.own ? '原创' : '转载'
        }
        return item
      })
      this.loading = false
    },

    // 翻页拉取数据
    handlePageChange(val) {
      this.pageNum = val
      this.fetchData()
    }
  }
}
</script>

<style scoped>
.admin-index-top-btn {
  display: flex;
  justify-content: space-between;
  margin: 12px 0;
  width: 170px;
}
</style>
