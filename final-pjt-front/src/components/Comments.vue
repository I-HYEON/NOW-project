<template>
  <div>
    
    <h3>댓글 작성</h3>
    <label for="content">내용 : </label>
    <input type="text" id="content" v-model="content" @keyup.enter="createComment">
    <button type="submit" id="content" @click="createComment">작성</button>

    <br>
    <template v-if="comments.filter(comment => comment.article === article.id).length === 0">
      <p>댓글이 없습니다.</p>
    </template>
    <template v-else>
      <p v-for="(comment, idx) in comments" :key="idx" v-if="comment.article === article?.id">
        댓글: {{ comment?.content }}
        <button @click="deleteComment(comment)">삭제</button>
      </p>
    </template>
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'Comments',
  data() {
    return {
      content: null,
      comments: this.$store.state.comments
    
    }
  },
  props: {
    article: Object,
  },
//   computed: {
//     comments() {
    
//       return this.$store.state.comments
      
//     },
//   },
  created() {
    this.getComments()
    // console.log(this.comments)
  },
  methods: {
    deleteComment(comment) {
      axios({
        method: 'delete',
        url: `${API_URL}/articles/comments/${comment.id}/`,
      })
        .then((response) => {
        console.log(response)
        // this.comments=response.data
        this.getComments()
        console.log(this.comments)
        })
        .catch((err) => {
          console.log(err);
        });
    },
    // getComments() {
    //   this.$store.dispatch('getComments')
    //   console.log(this.comme)
    // },
    getComments(){
      console.log('asdf')
      axios({
        method: 'get',
        url:  `${API_URL}/articles/comments/`
      })
      .then((res)=>{
        if (res.status === 404){
            console.log('fdkfd')
        }
        // console.log(res)
        this.comments=res.data
      })
      .catch(err => this.comments=null)
    },
    createComment() {
      const content = this.content
      if (this.content) {
        axios({
          method: 'post',
          url: `${API_URL}/articles/${this.$route.params.id}/comments/`,
          data: { content },
          headers:{
            Authorization: `Token ${this.$store.state.token}`
        },
        })
          .then(() => {
            this.content = null
            this.getComments()
          })
          .catch((err) => {
            console.log(err);
          });
      } else {
        alert('댓글을 입력하세요!')
      }
    },
  },
}
</script>

<style>

</style>
