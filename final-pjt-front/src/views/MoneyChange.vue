<template>
    <div class="container">
        <h2>환율 계산하기</h2>
        <div class="row g-3 align-items-center">
            <div class="col-auto">대한민국</div>
            <div class="col-auto"><input v-model="BeforeChange" class="form-control"></div>
            <div class="col-auto">
              <select class="form-select" aria-label="Default select example" v-model="Change">
                <option selected>나라를 선택해 주세요</option>
                <option v-for="(country, index) in Countrys" :value="ChangeInfo[index]" :key="index">{{ country }} {{ ChangeInfo[index].basePrice }}</option>
              </select>
            </div>
            <div class="col-auto"><input class="form-control" :value="Exchange.toFixed(2)"></div>
        </div>
        <br>
        <h2>환율 정보 확인</h2>
        <div class="row">
            <div class="mx-auto my-1 col-12 col-md-6 col-lg-4 col-xl-3" v-for="info in ChangeInfo" :key="info.index">
                <ChangeInfoCard :info="info" />
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';
import ChangeInfoCard from '@/components/ChangeInfoCard.vue';

export default {
name: 'MoneyChange',
components: {
    ChangeInfoCard,
},
data() {
    return {
    Countrys: [
        'USD', 'JPY', 'EUR', 'CNY', 'HKD', 'THB', 'TWD', 'PHP', 'SGD', 'AUD',
        'VND', 'GBP', 'CAD', 'MYR', 'RUB', 'ZAR', 'NOK', 'NZD', 'DKK', 'MXN',
        'MNT', 'BHD', 'BDT', 'BRL', 'BND', 'SAR', 'SEK', 'CHF', 'AED', 'JOD',
        'ILS', 'EGP', 'INR', 'IDR', 'CZK', 'KZT', 'QAR', 'KWD', 'TRY', 'PKR',
        'PLN'
    ],
    ChangeInfo: [],
    Change : 0,
    BeforeChange : 0,
    }
},
computed : {
    Exchange(){
        let rlt = this.BeforeChange/this.Change.basePrice*this.Change.currencyUnit
        if (isNaN(rlt)) return 0
        return rlt
    }
},
methods: {
    async Getdata() {
    const URL = 'https://quotation-api-cdn.dunamu.com/v1/forex/recent?codes=FRX.KRW';
    for (const country of this.Countrys) {
        const Get_URL = URL + country;
        const response = await axios.get(Get_URL);
        this.ChangeInfo.push(response.data[0]);
    }
    console.log(this.ChangeInfo);
    },
},
created() {
    this.Getdata();
},
};
</script>

<style>
.box-container {
display: flex;
justify-content: center;
}
.box {
width: 800px;
width: 800px;
border: 1px solid black;
}
.exchangecard {
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
}
</style>
  