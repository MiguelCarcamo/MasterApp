import React, { useState, useEffect } from 'react';
import { Container, Paper, Box, TextField, Grid, Button} from '@mui/material';
import LinearProgress from '@mui/material/LinearProgress';
import InformationBox from './InformationBox';
import axios from 'axios';
import swal from 'sweetalert';
import { ConstructionOutlined } from '@mui/icons-material';
import { Await } from 'react-router-dom';

function StyleBroad() {
    
    

    const [LineProcess, setLineProcess] = useState(true);
    const [file, setFile] = useState(false);
    const [BtnLook, setBtnLook] = useState(false);
    const [BtnLook2, setBtnLook2] = useState(true);

    const [DataCusto, setDataCusto] = useState(false);
    const [ChkCusto, setChkCusto] = useState(false);
    const [DataGlobalCat, setDataGlobalCat] = useState(false);
    const [ChkGlobalCat, setChkGlobalCat] = useState(false);
    const [DataWorkc, setDataWorkc] = useState(false);
    const [ChkWorkc, setChkWorkc] = useState(false);
    const [DataAllSty, setDataAllSty] = useState(false);
    const [ChkAllSty, setChkAllSty] = useState(false);
    const [DataSewSty, setDataSewSty] = useState(false);
    const [ChkSewSty, setChkSewSty] = useState(false);
    const [DataSewFam, setDataSewFam] = useState(false);
    const [ChkSewFam, setChkSewFam] = useState(false);
    const [DataSewLayout, setDataSewLayout] = useState(false);
    const [ChkSewLayout, setChkSewLayout] = useState(false);

    
    const [CustInfo, setCustInfo] = useState(0);
    const [CustInfoN, setCustInfoN] = useState(0);
    const [CustInfoU, setCustInfoU] = useState(0);
    const [GlobalInfo, setGlobalInfo] = useState(0);
    const [GlobalInfoN, setGlobalInfoN] = useState(0);
    const [GlobalInfoU, setGlobalInfoU] = useState(0);    
    const [WorkceInfo, setWorkceInfo] = useState(0);
    const [WorkceInfoN, setWorkceInfoN] = useState(0);
    const [WorkceInfoU, setWorkceInfoU] = useState(0);
    const [GeneralInfInfo, setGeneralInfInfo] = useState(0);
    const [GeneralInfInfoN, setGeneralInfInfoN] = useState(0);
    const [GeneralInfInfoU, setGeneralInfInfoU] = useState(0);
    const [GeneralSew, setGeneralSew] = useState(0);
    const [GeneralSewN, setGeneralSewN] = useState(0);
    const [GeneralSewU, setGeneralSewU] = useState(0);
    const [GeneralSewFam, setGeneralSewFam] = useState(0);
    const [GeneralSewFamN, setGeneralSewFamN] = useState(0);
    const [GeneralSewFamU, setGeneralSewFamU] = useState(0);
    const [GeneralSewLayout, setGeneralSewLayout] = useState(0);
    const [GeneralSewLayoutN, setGeneralSewLayoutN] = useState(0);
    const [GeneralSewLayoutU, setGeneralSewLayoutU] = useState(0);        

    let url2 = "https://arnpythondev.tegraglobal.com:5000/api/File/";
    let customConfig = {
        headers: {
            'Content-Type': 'application/json'
        }
    };
    const FileCustomer = async () =>{
        try{
            const form = new FormData();
            form.append('File', file);
            const Cust = await axios({method: "post",url: url2 + "StyleCustumer",data: form, headers: { "Content-Type": "multipart/form-data" },});
            if(Cust.data.length > 0){
                setDataCusto(Cust.data);
                setCustInfo(Cust.data.length);
                setCustInfoN(Cust.data.filter(i=> i.id === 0).length);
                setCustInfoU(Cust.data.filter(i=> i.id !== 0).length);
                var datax = JSON.stringify(Cust.data);
                var url = "https://arnpythondev.tegraglobal.com:5000/api/Style_Customer/add/1";
                const x = await axios.post(url, datax, customConfig);
                if(x.data['msj']='Accion Realizada Correctamente'){
                    setChkCusto(true);
                }
            }
        }catch(err) {
            setLineProcess(true);
        }
    }
    const FileGlobalCategory = async () =>{
        try{
            const form = new FormData();
            form.append('File', file);
            const Global = await axios({method: "post",url: url2 + "StyleGlobalCategory",data: form,headers: { "Content-Type": "multipart/form-data" },});
            if(Global.data.length > 0){
                setDataGlobalCat(Global.data);
                setGlobalInfo(Global.data.length);
                setGlobalInfoN(Global.data.filter(i=> i.id === 0).length);
                setGlobalInfoU(Global.data.filter(i=> i.id !== 0).length);
                var datax = JSON.stringify(Global.data);
                var url = "https://arnpythondev.tegraglobal.com:5000/api/Style_GlobalCategory/add/1";
                await axios.post(url, datax, customConfig);
                setChkGlobalCat(true);
            }
            setLineProcess(true);
        }catch(err) {
            setLineProcess(true);
        }
    }
    const FileWorkcenter = async () =>{
        try{
            const form = new FormData();
            form.append('File', file);
            const Workce = await axios({method: "post",url: url2 + "StyleWorkcenter",data: form,headers: { "Content-Type": "multipart/form-data" },});
            if(Workce.data.length > 0){
                setDataWorkc(Workce.data);
                setWorkceInfo(Workce.data.length);
                setWorkceInfoN(Workce.data.filter(i=> i.id === 0).length);
                setWorkceInfoU(Workce.data.filter(i=> i.id !== 0).length);
                var datax = JSON.stringify(Workce.data);
                var url = "https://arnpythondev.tegraglobal.com:5000/api/Style_Workcenter/add/1";
                await axios.post(url, datax, customConfig);
                setChkWorkc(true);
            }
            setLineProcess(true);
        }catch(err) {
            setLineProcess(true);
        }
    }
    const FileGeneralInfo = async () =>{
        try{
            const form = new FormData();
            form.append('File', file);
            const GeneralInf = await axios({method: "post",url: url2 + "StyleGeneral",data: form,headers: { "Content-Type": "multipart/form-data" },});
            if(GeneralInf.data.length > 0){
                setDataAllSty(GeneralInf.data);
                setGeneralInfInfo(GeneralInf.data.length);
                setGeneralInfInfoN(GeneralInf.data.filter(i=> i.id === 0).length);
                setGeneralInfInfoU(GeneralInf.data.filter(i=> i.id !== 0).length);
                var datax = JSON.stringify(GeneralInf.data);
                var url = "https://arnpythondev.tegraglobal.com:5000/api/Style_GeneralInfo/add/1";
                await axios.post(url, datax, customConfig);
                setChkAllSty(true);
            }
            setLineProcess(true);
        }catch(err) {
            setLineProcess(true);
        }
    }
    const FileSewGeneralInfo = async () =>{
        try{
            const form = new FormData();
            form.append('File', file);
            const GeneralSewInf = await axios({method: "post",url: url2 + "StyleSewInfo",data: form,headers: { "Content-Type": "multipart/form-data" },});
            if(GeneralSewInf.data.length > 0){
                setDataSewSty(GeneralSewInf.data);
                setGeneralSew(GeneralSewInf.data.length);
                setGeneralSewN(GeneralSewInf.data.filter(i=> i.id === 0).length);
                setGeneralSewU(GeneralSewInf.data.filter(i=> i.id !== 0).length);
                var datax = JSON.stringify(GeneralSewInf.data);
                var url = "https://arnpythondev.tegraglobal.com:5000/api/Style_Sewing/add/1";
                await axios.post(url, datax, customConfig);
                setChkSewSty(true);
            }
            setLineProcess(true);
        }catch(err) {
            setLineProcess(true);
        }
    }
    const FileSewGeneralFam = async () =>{
        try{
            const form = new FormData();
            form.append('File', file);
            const GeneralSewFam_ = await axios({method: "post",url: url2 + "StyleSewFamily",data: form,headers: { "Content-Type": "multipart/form-data" },});
            if(GeneralSewFam_.data.length > 0){
                setDataSewFam(GeneralSewFam_.data);
                setGeneralSewFam(GeneralSewFam_.data.length);
                setGeneralSewFamN(GeneralSewFam_.data.filter(i=> i.id === 0).length);
                setGeneralSewFamU(GeneralSewFam_.data.filter(i=> i.id !== 0).length);
                var datax = JSON.stringify(GeneralSewFam_.data);
                var url = "https://arnpythondev.tegraglobal.com:5000/api/Style_Sewing_Family/add/1";
                await axios.post(url, datax, customConfig);
                setChkSewFam(true);
            }
            setLineProcess(true);
        }catch(err) {
            setLineProcess(true);
        }
    }
    const FileSewGeneralLay = async () =>{
        try{
            const form = new FormData();
            form.append('File', file);
            const GeneralSewLay = await axios({method: "post",url: url2 + "StyleSewLayout",data: form,headers: { "Content-Type": "multipart/form-data" },});
            if(GeneralSewLay.data.length > 0){
                setDataSewLayout(GeneralSewLay.data);
                setGeneralSewLayout(GeneralSewLay.data.length);
                setGeneralSewLayoutN(GeneralSewLay.data.filter(i=> i.id === 0).length);
                setGeneralSewLayoutU(GeneralSewLay.data.filter(i=> i.id !== 0).length);
                var datax = JSON.stringify(GeneralSewLay.data);
                var url = "https://arnpythondev.tegraglobal.com:5000/api/Style_Sewing_LayoutConfiguration/add/1";
                await axios.post(url, datax, customConfig);
                setChkSewLayout(true);
            }
            setLineProcess(true);
        }catch(err) {
            setLineProcess(true);
        }
    }
    const resetChk = () =>{
        setChkCusto(false);
        setChkGlobalCat(false);
        setChkWorkc(false);
        setChkAllSty(false);
        setChkSewSty(false);
        setChkSewFam(false);
        setChkSewLayout(false);
    }
    
    const UploadFile = async () =>  {
        setLineProcess(false);
        resetChk();
        FileCustomer();
        
    }
    useEffect(() => {
        if(ChkCusto){
            FileGlobalCategory();
        }
    }, [ChkCusto]);
    useEffect(() => {
        if(ChkGlobalCat){
            FileWorkcenter();
        }
    }, [ChkGlobalCat]);
    useEffect(() => {
        if(ChkWorkc){
            FileGeneralInfo();
        }
    }, [ChkWorkc]);
    useEffect(() => {
        if(ChkAllSty){
            FileSewGeneralFam();
        }
    }, [ChkAllSty]);
    useEffect(() => {
        if(ChkSewFam){
            FileSewGeneralLay();
        }
    }, [ChkSewFam]);
    useEffect(() => {
        if(ChkAllSty && ChkSewLayout){
            FileSewGeneralInfo();
        }
    }, [ChkAllSty, ChkSewLayout]);
    useEffect(() => {
        if(ChkSewLayout){
            setLineProcess(true);
            swal("Good job!", "You clicked the button!", "success");
        }
    }, [ChkSewLayout]);

  return (
    <Container component="main" maxWidth="lg" sx={{ mb: 4 }}>
        <Paper variant="outlined" sx={{ my: { xs: 4, md: 7 }, p: { xs: 3, md: 4 } }}>
            <Box hidden={LineProcess} sx={{ width: '100%' }}>
                <LinearProgress />
            </Box>
            <Container maxWidth="lg" sx={{ mt: 4, mb: 4 }}>
                <Grid container spacing={3}>
                    <InformationBox color='#FA6E59' title='Customer' num={50} num2={CustInfo} new={CustInfoN} Update={CustInfoU} val={ChkCusto}/>
                    <InformationBox color='#68829E' title='Global Category' num={40} num2={GlobalInfo} new={GlobalInfoN} Update={GlobalInfoU} val={ChkGlobalCat} />
                    <InformationBox color='#AEBD38' title='Workcenter' num={30} num2={WorkceInfo} new={WorkceInfoN} Update={WorkceInfoU} val={ChkWorkc}/>
                    <InformationBox color='#598234' title='All Styles' num={120} num2={GeneralInfInfo} new={GeneralInfInfoN} Update={GeneralInfInfoU} val={ChkAllSty} />
                </Grid>
            </Container>
            <Container maxWidth="lg" sx={{ mt: 4, mb: 4 }}>
                <Grid container spacing={3}>
                    <InformationBox color='#D13525' title='Sew Style' num={50} num2={GeneralSew} new={GeneralSewN} Update={GeneralSewU} val={ChkSewSty}/>
                    <InformationBox color='#2988BC' title='Sew Family' num={40} num2={GeneralSewFam} new={GeneralSewFamN} Update={GeneralSewFamU} val={ChkSewFam} />
                    <InformationBox color='#7e7b15' title='Sew Layout Config' num={30} num2={GeneralSewLayout} new={GeneralSewLayoutN} Update={GeneralSewLayoutU} val={ChkSewLayout} />
                </Grid>
            </Container>
            <Grid item xs={12} sm={8}>
                <TextField type="File" onChange={(e) => setFile(e.target.files[0]) } fullWidth />
                <Button disabled={BtnLook} onClick={UploadFile} variant="contained" style={{ backgroundColor: '#00A9EO' }}>Upload File</Button>
            </Grid>
        </Paper>
    </Container>
  )
}

export default StyleBroad