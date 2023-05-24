<template>
  <div class="container-fluid">
    <div class="row justify-content-center">
      <div class="col-12">
        <div class="d-flex justify-content-center flex-wrap">
          <div v-if="show" class="row mx-0">
          <img src='@/photo/png/pig_and_dog.png' alt="main_img" style="max-width:100%; height:auto;">
            <DepositCard
              class="mx-auto my-1 col-12 col-md-6 col-lg-4 col-xl-3"
              v-for="deposit in $store.state.depositData"
              :deposit="deposit"
              :key="deposit.id"
            />
          </div>
          <div v-else>
            <img src="@/photo/loading.gif" alt="로딩중..." />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import DepositCard from '@/components/DepositCard.vue'
import axios from 'axios'

export default {
  name: 'DepositProducts',
  data() {
    return {
      show: false,
    }
  },
  components: {
    DepositCard,
  },
  methods: {
    async getDepositData() {
      const response = await axios.get('http://127.0.0.1:8000/deposits/save/')
      this.$store.commit('GET_DEPOSIT_DATA', response.data)
      this.show = true
    },
  },
  created() {
    this.getDepositData()
  },
}
</script>

<style scoped>
.container-fluid {
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
}

.d-flex {
  margin-top: 20px;
}

.row.mx-0 {
  margin-left: -20px;
  margin-right: -20px;
}

.col-12,
.col-md-6,
.col-lg-4,
.col-xl-3 {
  margin: 20px;
}

.DepositCard {
  position: relative;
  overflow: hidden;
  background-color: #fff;
  border-radius: 10px;
  box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.3);
  transition: transform 0.3s, box-shadow 0.3s;
  /* margin-bottom: 20px; */
}

.DepositCard:hover {
  transform: scale(1.1);
  box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.3);
}

.DepositCard .card-img-top {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.DepositCard .card-body {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  background-color: rgba(255, 255, 255, 0.8);
  padding: 10px;
}

.DepositCard .card-title {
  font-size: 1rem;
  font-weight: bold;
}

.DepositCard .list-group-item {
  text-align: center;
}

.DepositCard .explain {
  font-size: 0.8rem;
  color: #333;
}

.DepositCard .link {
  text-decoration-line: none;
  color: #333;
}

</style>
