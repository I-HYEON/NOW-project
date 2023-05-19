<template>
  <div class="article-list">
    <h3>Article List</h3>
    <ArticleListItem 
    v-for="article in articles" :key="article.id" :article="article"
    />
  </div>
</template>

<script>
import ArticleListItem from '@/components/ArticleListItem'
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'ArticleList',
  components: {
    ArticleListItem,
  },
  data(){
    return {
      articles:null
    }
  },
  methods:{
    getArticles(){
      axios({
        method: 'get',
        url : `${API_URL}/articles/`
      })
      .then((res)=> {
        this.articles = res.data
        console.log(res.data)
      })
      .catch(err => console.log(err))
    }
  },
  // computed: {
  //   articles() {
  //     return this.$store.state.articles
  //   }
  // },
  created(){
    this.getArticles()

  },
}
</script>

<style>
.article-list {
  text-align: start;
}
</style>
