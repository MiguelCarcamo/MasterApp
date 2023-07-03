import React, { useState, useEffect } from 'react';
import { PowerBIEmbed } from 'powerbi-client-react';
import Grid from '@mui/material/Grid';
import TextField from '@mui/material/TextField';
import Autocomplete from '@mui/material/Autocomplete';
import { models} from 'powerbi-client';
import axios from 'axios';
import './PowerBiPlanning.css'

function PowerBiPlanning() {
    const [Token, setToken] = useState(false);
    const [Process, setProcess] = useState("Sewing");
    const [Position, setPosition] = useState(1);
    const [ProcessData, setProcessData] = useState([
        {proces:'Sewing', id:'521f83a6-5be7-46cd-9460-3ac01dd4c943', url:'https://app.powerbi.com/reportEmbed?reportId=521f83a6-5be7-46cd-9460-3ac01dd4c943&groupId=bf2b79b7-7653-4250-98e0-846627acf5b4&w=2&config=eyJjbHVzdGVyVXJsIjoiaHR0cHM6Ly9XQUJJLVVTLUVBU1QyLUMtUFJJTUFSWS1yZWRpcmVjdC5hbmFseXNpcy53aW5kb3dzLm5ldCIsImVtYmVkRmVhdHVyZXMiOnsibW9kZXJuRW1iZWQiOnRydWUsInVzYWdlTWV0cmljc1ZOZXh0Ijp0cnVlfX0%3d'},
        {proces:'Cutting', id:'10bd1804-37d6-46e0-913d-4000eb261700', url:'https://app.powerbi.com/reportEmbed?reportId=10bd1804-37d6-46e0-913d-4000eb261700&groupId=bf2b79b7-7653-4250-98e0-846627acf5b4&w=2&config=eyJjbHVzdGVyVXJsIjoiaHR0cHM6Ly9XQUJJLVVTLUVBU1QyLUMtUFJJTUFSWS1yZWRpcmVjdC5hbmFseXNpcy53aW5kb3dzLm5ldCIsImVtYmVkRmVhdHVyZXMiOnsibW9kZXJuRW1iZWQiOnRydWUsInVzYWdlTWV0cmljc1ZOZXh0Ijp0cnVlfX0%3d'},
        {proces:'Heat Transfer', id:'7f08a2e0-ba47-4cf1-ba8c-ad34a0bc09bc', url:'https://app.powerbi.com/reportEmbed?reportId=7f08a2e0-ba47-4cf1-ba8c-ad34a0bc09bc&groupId=bf2b79b7-7653-4250-98e0-846627acf5b4&w=2&config=eyJjbHVzdGVyVXJsIjoiaHR0cHM6Ly9XQUJJLVVTLUVBU1QyLUMtUFJJTUFSWS1yZWRpcmVjdC5hbmFseXNpcy53aW5kb3dzLm5ldCIsImVtYmVkRmVhdHVyZXMiOnsibW9kZXJuRW1iZWQiOnRydWUsInVzYWdlTWV0cmljc1ZOZXh0Ijp0cnVlfX0%3d'},
        {proces:'Pad Printing', id:'d076ebbb-9082-43ee-b046-18d35aa7c575', url:'https://app.powerbi.com/reportEmbed?reportId=d076ebbb-9082-43ee-b046-18d35aa7c575&groupId=bf2b79b7-7653-4250-98e0-846627acf5b4&w=2&config=eyJjbHVzdGVyVXJsIjoiaHR0cHM6Ly9XQUJJLVVTLUVBU1QyLUMtUFJJTUFSWS1yZWRpcmVjdC5hbmFseXNpcy53aW5kb3dzLm5ldCIsImVtYmVkRmVhdHVyZXMiOnsibW9kZXJuRW1iZWQiOnRydWUsInVzYWdlTWV0cmljc1ZOZXh0Ijp0cnVlfX0%3d'},
        {proces:'Namaplate', id:'a5c600a2-6f8b-4044-9f09-afda45b96bad', url:'https://app.powerbi.com/reportEmbed?reportId=a5c600a2-6f8b-4044-9f09-afda45b96bad&groupId=bf2b79b7-7653-4250-98e0-846627acf5b4&w=2&config=eyJjbHVzdGVyVXJsIjoiaHR0cHM6Ly9XQUJJLVVTLUVBU1QyLUMtUFJJTUFSWS1yZWRpcmVjdC5hbmFseXNpcy53aW5kb3dzLm5ldCIsImVtYmVkRmVhdHVyZXMiOnsibW9kZXJuRW1iZWQiOnRydWUsInVzYWdlTWV0cmljc1ZOZXh0Ijp0cnVlfX0%3d'},
        {proces:'Consolidate', id:'68a40cf3-41e3-4378-a63e-33b5c44fc114', url:'https://app.powerbi.com/reportEmbed?reportId=68a40cf3-41e3-4378-a63e-33b5c44fc114&groupId=bf2b79b7-7653-4250-98e0-846627acf5b4&w=2&config=eyJjbHVzdGVyVXJsIjoiaHR0cHM6Ly9XQUJJLVVTLUVBU1QyLUMtUFJJTUFSWS1yZWRpcmVjdC5hbmFseXNpcy53aW5kb3dzLm5ldCIsImVtYmVkRmVhdHVyZXMiOnsibW9kZXJuRW1iZWQiOnRydWUsInVzYWdlTWV0cmljc1ZOZXh0Ijp0cnVlfX0%3d'},
        {proces:'Consolidate Cutting', id:'99168ee5-4e01-4988-9e24-6d5f720b7b0d', url:'https://app.powerbi.com/reportEmbed?reportId=99168ee5-4e01-4988-9e24-6d5f720b7b0d&groupId=bf2b79b7-7653-4250-98e0-846627acf5b4&w=2&config=eyJjbHVzdGVyVXJsIjoiaHR0cHM6Ly9XQUJJLVVTLUVBU1QyLUMtUFJJTUFSWS1yZWRpcmVjdC5hbmFseXNpcy53aW5kb3dzLm5ldCIsImVtYmVkRmVhdHVyZXMiOnsibW9kZXJuRW1iZWQiOnRydWUsInVzYWdlTWV0cmljc1ZOZXh0Ijp0cnVlfX0%3d'},
    ]);
    const UpdateToken = async () =>  {
        try {
            const data = await axios("https://arnpythondev.tegraglobal.com:5000/api/General_GetTokenPowerBi/");
            if (data.status == 200){
                const data1 = await data.data.access_token;
                setToken(data1);
            }
        } catch (error) {
           console.log(error); 
        }
    }
    useEffect(() => {
        const run = async () =>
            await UpdateToken();
        run();
    }, []);
    useEffect(() => {
        if (Process == "Sewing"){
            setPosition(0);
        }else if(Process == "Cutting"){
            setPosition(1);
        }else if(Process == "Heat Transfer"){
            setPosition(2);
        }else if(Process == "Pad Printing"){
            setPosition(3);
        }else if(Process == "Namaplate"){
            setPosition(4);
        }
        else if(Process == "Consolidate"){
            setPosition(5);
        }
        else if(Process == "Consolidate Cutting"){
            setPosition(6);
        }
    }, [Process]);
// 
  return (
    <div style={{ height: '100%', width: '100%' }}>
        <Grid item xs={10} sm={4}>
            <Autocomplete
                onChange={(event, newValue) => {
                    setProcess(newValue);
                }}
                value={Process}
                options={(ProcessData)?ProcessData.map((option) =>option.proces):[]}
                renderInput={(params) => <TextField {...params} label="Process" />}
            />
        </Grid>
        {Token != ""?
        <PowerBIEmbed
            embedConfig = {{
                type: 'report',   // Supported types: report, dashboard, tile, visual and qna
                id: ProcessData[Position].id,
                embedUrl: ProcessData[Position].url,
                accessToken: Token,
                tokenType: models.TokenType.Aad,
                settings: {
                    panes: {
                        filters: {
                            expanded: false,
                            visible: false
                        }
                    },
                }
            }}

            eventHandlers = { 
                new Map([
                    ['loaded', function () {console.log('Report loaded');}],
                    ['rendered', function () {console.log('Report rendered');}],
                    ['error', function (event) {console.log(event.detail);}]
                ])
            }
                
            cssClassName = { "Embed-container" }

            getEmbeddedComponent = { (embeddedReport) => {
                window.report = embeddedReport;
            }}
        />
        :false
        }
    </div>    
  )
}

export default PowerBiPlanning