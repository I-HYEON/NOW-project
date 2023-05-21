<template> 
<div> <h3>댓글 작성</h3>
<label for="content">내용 :
</label>
<input type="text" id="content" v-model="content" @keyup.enter="createComment">
    <button type="submit" id="content" @click="createComment">작성</button>

    <br>
        <template v-if="comments.filter(comment => comment.depositproducts === deposit_detail.id).length === 0">
            <p>댓글이 없습니다.</p>
        </template>
        <template v-else="v-else">
            <p
                v-for="(comment, idx) in comments"
                :key="idx"
                v-if="comment.depositproducts === deposit_detail.id">
                댓글: {{ comment?.content }}
                {{ comment?.username }}
                {{deposit_detail.fin_prdt_cd}}
                <button @click="deleteComment(comment)">삭제</button>
            </p>
            <!-- <p
                v-for="(comment, idx) in comments"
                :key="idx"
>
                댓글: {{ comment?.content }}
                {{deposit_detail.id}}
                <button @click="deleteComment(comment)">삭제</button>
            </p> -->
        </template>
    </div>
</template>

<script>
    import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
    name: 'DepositComments',
    data() {
    return {
    content: null,
    comments: this.$store.state.comments
    
    }
    },
    props: {
    deposit_detail: Object,
    article: Object,
}  ,

  created() {
    this.getComments()
    // console.log(this.comments)
  },
  methods: {
    deleteComment(comment) {
      axios({
        method: 'delete',
        url: `${API_URL}/deposits/comments/${comment.id}/`,
      })
        .then((response) => {
        console.log(response)
        this.getComments()
        console.log(this.comments)
        })
        .catch((err) => {
          console.log(err);
        });
    },

    getComments(){
      // console.log('asdf')
      axios({
        method: 'get',
        url:  `${API_URL}/deposits/comments/`
      })
      .then((res)=>{
        if (res.status === 404){
            console.log('fdkfd')
        }
        this.comments=res.data
        console.log(this.comments)
      })
      .catch(err => this.comments=null)
    },
    createComment() {
      //보낼때는 해당 deposit_detail의 fin_prdt_cd가 unique라서 구분자로 쓸 수 있고, 
      //위에서 해당 deposit_detail의 id를 통해 해당 상품의 댓글인지 필터링할 수 있었다. 
      //deposit_detail에 id넣어줘서 고맙다 성환아 ㅠㅠ
      const content = this.content
      if (this.content) {
        axios({
          method: 'post',
          url: `${API_URL}/deposits/${this.deposit_detail.fin_prdt_cd}/comments/`,
          data: { content },
          headers:{
            Authorization: `Token ${this.$store.state.token}`}
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
