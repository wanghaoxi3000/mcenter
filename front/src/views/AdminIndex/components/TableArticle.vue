<template>
  <div>
    <Table
      stripe
      border
      :loading="loadingStatus"
      :columns="columnsList"
      :data="value">
    </Table>


    <Page :total="valueNum" show-sizer :placement="'top'" class-name="page-center"></Page>

  </div>
</template>

<script>
const editButton = (vm, h, currentRow, index) => {
  return h('Button', {
    props: {
      type: currentRow.editting ? 'success' : 'primary',
      loading: currentRow.saving
    },
    style: {
      margin: '0 5px'
    },
    on: {
      'click': () => {
        if (!currentRow.editting) {
          if (currentRow.edittingCell) {
            for (let name in currentRow.edittingCell) {
              if (currentRow.edittingCell.hasOwnProperty(name)) {
                currentRow.edittingCell[name] = false
                vm.edittingStore[index].edittingCell[name] = false
              }

            }
          }
          vm.edittingStore[index].editting = true
          vm.thisTableData = JSON.parse(JSON.stringify(vm.edittingStore))
        } else {
          vm.edittingStore[index].saving = true
          vm.thisTableData = JSON.parse(JSON.stringify(vm.edittingStore))
          let edittingRow = vm.edittingStore[index]
          edittingRow.editting = false
          edittingRow.saving = false
          vm.thisTableData = JSON.parse(JSON.stringify(vm.edittingStore))
          vm.$emit('input', vm.handleBackdata(vm.thisTableData))
          vm.$emit('on-change', vm.handleBackdata(vm.thisTableData), index)
        }
      }
    }
  }, currentRow.editting ? '保存' : '编辑')
}

const deleteButton = (vm, h, currentRow, index) => {
  return h('Poptip', {
    props: {
      confirm: true,
      title: '您确定要删除这条数据吗?',
      transfer: true
    },
    on: {
      'on-ok': () => {
        vm.thisTableData.splice(index, 1)
        vm.$emit('input', vm.handleBackdata(vm.thisTableData))
        vm.$emit('on-delete', vm.handleBackdata(vm.thisTableData), index)
      }
    }
  }, [
    h('Button', {
      style: {
        margin: '0 5px'
      },
      props: {
        type: 'error',
        placement: 'top'
      }
    }, '删除')
  ])
}

export default {
  name: 'tableArticle',
  props: {
    columnsList: Array,   // 表格列的配置描述
    value: Array,         // 显示的结构化数据
    valueNum: {           // 数据总数
      type: Number,
      default: 0
    },
    loadingStatus: {      // 表格是否加载中
      type: Boolean,
      default: false
    }
  },

  data() {
    return {
      thisTableData: [
        {
          title: '博客文章',
          source: '原创',
          category: '类别',
          time: '2018-01-08',
          num: '10'
        },
        {
          title: '博客文章2',
          source: '原创',
          category: '类别',
          time: '2018-01-08',
          num: '10'
        },
        {
          title: '博客文章3',
          source: '原创',
          category: '类别',
          time: '2018-01-08',
          num: '10'
        }
      ]
    }
  },
  created() {
    this.init()
  },
  methods: {
    // 为包含handle的列添加编辑或删除按钮
    init() {
      this.columnsList.forEach(item => {
        if (item.handle) {
          item.render = (h, param) => {
            let currentRowData = this.thisTableData[param.index]
            if (item.handle.length === 2) {
              return h('div', [
                editButton(this, h, currentRowData, param.index),
                deleteButton(this, h, currentRowData, param.index)
              ])
            } else if (item.handle.length === 1) {
              if (item.handle[0] === 'edit') {
                return h('div', [
                  editButton(this, h, currentRowData, param.index)
                ])
              } else {
                return h('div', [
                  deleteButton(this, h, currentRowData, param.index)
                ])
              }
            }
          }
        }
      })
    }
  }
}
</script>

<style scoped>
.page-center{
  margin-top: 30px;
  text-align: center;
}
</style>
