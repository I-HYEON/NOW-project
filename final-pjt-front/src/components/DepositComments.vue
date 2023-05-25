<template>
  <div>
    <div v-show="isLogin">
      <h3>댓글 작성</h3>
      <textarea id="content" placeholder="댓글을 입력하세요" style="width: 600px;" rows="5" v-model="content" @keyup.enter="createComment"></textarea><br>
      <button type="button" id="content" @click="createComment" class="btn btn-outline-success">작성</button>
    </div>
    <br>

    <br>
    <template v-if="comments.filter(comment => comment.depositproducts === deposit_detail.id).length === 0">
      <p>댓글이 없습니다.</p>
    </template>
    <template v-else="v-else">
      <div v-for="(comment, idx) in comments" :key="idx" v-if="comment.depositproducts === deposit_detail.id">
        <div style="display: flex; align-items: center; justify-content: space-between;">
          <div>
            {{comment?.username}} : {{ comment?.content }}
            <hr>
          </div>
          <div>
            <template v-if="editingCommentId !== comment.id">
              <span @click="editComment(comment)">수정</span> |
              <span @click="deleteComment(comment)">삭제</span>
            </template>
            <template v-else>
              <input type="text" v-model="editedContent" @keyup.enter="updateComment(comment)">
              <button @click="updateComment(comment)">저장</button>
              <button @click="cancelEdit">취소</button>
            </template>
          </div>
        </div>
      </div>
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
      comments: this.$store.state.comments,
      editingCommentId: null,
      editedContent: ''
    }
  },
  props: {
    deposit_detail: Object,
  },
  created() {
    this.getComments()
  },
  computed: {
    isLogin() {
      return this.$store.getters.isLogin
    },
    userInfo() {
      return this.$store.state.userInfo
    }
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
        })
        .catch((err) => {
          console.log(err);
        });
    },
    editComment(comment) {
      this.editingCommentId = comment.id
      this.editedContent = comment.content
    },

    updateComment(comment) {
      axios({
        method: 'put',
        url: `${API_URL}/deposits/comments/${comment.id}/`,
        data: { content: this.editedContent },
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
        .then(() => {
          this.editingCommentId = null
          this.editedContent = ''
          this.getComments()
        })
        .catch((err) => {
          console.log(err);
        });
    },

    cancelEdit() {
      this.editingCommentId = null
      this.editedContent = ''
    },

    getComments() {
      axios({
        method: 'get',
        url: `${API_URL}/deposits/comments/`
      })
        .then((res) => {
          if (res.status === 404) {
            console.log('fdkfd')
          }
          this.comments = res.data
        })
        .catch(err => this.comments = null)
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
          headers: {
            Authorization: `Token ${this.$store.state.token}`
          }
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
.button-wrapper {
  margin-right: 30px;
}
</style>
