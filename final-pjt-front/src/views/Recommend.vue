<template>
  <div class="d-flex flex-column align-items-center justify-content-center">
    <img src='@/photo/png/pig_and_dog.png' alt="main_img" style="max-width:100%; height:auto;">
    <table class="table" border="1">
        <th></th>
        <tr>
            <td>성별</td>
            <td>
                <input type="checkbox" name="tendency" v-model="info.gen_two">여자        
                <input type="checkbox" name="tendency" v-model="info.gen_one">남자
            </td>
            
        </tr>
        <tr>
            <td>나이</td>
            <td>
                <input type="checkbox" name="tendency" v-model="info.age_one">20세 미만       
                <input type="checkbox" name="tendency" v-model="info.age_two">20세 ~ 29세
                <input type="checkbox" name="tendency" v-model="info.age_thr">30세 ~ 39세
                <input type="checkbox" name="tendency" v-model="info.age_fou">40세 ~ 49세
                <input type="checkbox" name="tendency" v-model="info.age_fiv">50세 ~ 59세
                <input type="checkbox" name="tendency" v-model="info.age_six">60세 이상
            </td>
        </tr>
        <tr>
            <td>연봉</td>
            <td>
                <input type="checkbox" name="tendency" v-model="info.sal_one">2000만원 미만
                <input type="checkbox" name="tendency" v-model="info.sal_two">2000만원 ~ 4000만원
                <input type="checkbox" name="tendency" v-model="info.sal_thr">4000만원 ~ 6000만원
                <input type="checkbox" name="tendency" v-model="info.sal_fou">6000만원 ~ 8000만원
                <input type="checkbox" name="tendency" v-model="info.sal_fiv">8000만원 ~ 1억원
                <input type="checkbox" name="tendency" v-model="info.sal_six">1억원 이상
            </td>
        </tr>
        <tr>
            <td>자산</td>
            <td>
                <input type="checkbox" name="tendency" v-model="info.whl_one">2000만원 미만
                <input type="checkbox" name="tendency" v-model="info.whl_two">2000만원 ~ 6000만원
                <input type="checkbox" name="tendency" v-model="info.whl_thr">6000만원 ~ 1억원
                <input type="checkbox" name="tendency" v-model="info.whl_fou">1억원 ~ 2억원
                <input type="checkbox" name="tendency" v-model="info.whl_five">2억원 ~ 4억원
                <input type="checkbox" name="tendency" v-model="info.whl_six">4억원 이상
            </td>
        </tr>
        <tr>
            <td>저축성향</td>
            <td>
                <input type="checkbox" name="tendency" v-model="info.ten_one">단기
                <input type="checkbox" name="tendency" v-model="info.ten_two">중기
                <input type="checkbox" name="tendency" v-model="info.ten_thr">장기
            </td>
        </tr>
    </table>
    <div class="container">
        <div v-if=show class="row justify-content-center">
            <div v-if="dataLength">
                <p class="text-center">선택하신 조건과 일치하는 회원들이 선호하는 상품들을 둘러보세요!</p>
            </div>
            <div class="row" v-else>
                <p>선택하신 조건과 일치하는 상품이 존재하지 않습니다. 대신 이런상품은 어떤가요?</p>
                <DepositCard
                class = "mx-auto my-1 col-12 depositcard"
                v-for="deposit in this.high_income_depositData"
                :deposit="deposit"
                :key="deposit.id"
                />
            </div>
            <DepositCard
            class = "mx-auto my-1 col-12 depositcard"
            v-for="deposit in this.sorted_depositData"
            :deposit="deposit"
            :key="deposit.id"
            />
        </div>
        <div v-else>
            <div class="loading-container">
              <div class="loader"></div>
            </div>
        </div>
    </div>
    </div>
</template>

<script>
import axios from 'axios'
import DepositCard from '@/components/DepositCard.vue'
const API_URL = 'http://127.0.0.1:8000'

export default {
    name: 'Recommend',
    components: {
        DepositCard
    },
    data(){
        return {
            show : false,
            sorted_depositData : [],
            high_income_depositData : [],
            info : {
            gen_one : false, gen_two : false,
            age_one : false, age_two : false, age_thr : false, age_fou : false, age_five : false, age_six : false,
            sal_one : false, sal_two : false, sal_thr : false, sal_fou : false, sal_five : false, sal_six : false,
            whl_one : false, whl_two : false, whl_thr : false, whl_fou : false, whl_five : false, whl_six : false,
            ten_one : false, ten_two : false, ten_thr : false
            },
        }
    },
    methods : {
        get_deposit_sorted() {
            const info = this.info
            axios({
                method: 'POST',
                url: `${API_URL}/deposits/recomend_deposit/`,
                data: info,
            })
            .then((response) => {
                this.sorted_depositData = response.data[1]
                this.high_income_depositData = response.data[0]
                console.log(this.sorted_depositData)
                console.log(this.high_income_depositData)
                this.show = true
            })
            .catch((err) => {
            console.log(err)
            })
        }
    },
    watch : {
      info : {
        handler(val,oldval) {
            this.show = false
            this.get_deposit_sorted()
        },
        deep:true,
      }
    },
    created() {
        this.get_deposit_sorted()
    },
    computed: {
    dataLength() {
        const length = Object.keys(this.sorted_depositData).length
        return length
        }
    }
}
</script>

<style>

.table {
  max-width: 1270px;
  width: 90% !important;
  margin-left: 20px;
  margin-right: 20px;
}

.loading{
    width: 100%;
    height: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
}

th,
td {
    text-align: center;
}

.loading-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
}

.loader {
  width: 100px;
  height: 100px;
  border: 10px solid rgba(0, 0, 0, 0.2);
  border-top-color: #000;
  border-radius: 50%;
  animation: spin 2s linear infinite;
}

.depositcard {
  min-width: 200px;
}

@keyframes spin {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}

</style>