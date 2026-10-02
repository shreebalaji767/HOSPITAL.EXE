/* HOSPITAL.EXE facility expansion engine */
(()=>{
 const source=window.HOSPITAL_CONTENT?.facilityComics||[];
 const modes=[
  (f,t,p)=>[f,t+" // INCIDENT LOG",["INCIDENT LOG: "+p[0],"STATUS: "+p[1],"SUPERVISOR: "+p[2],"VERDICT: "+p[3]]],
  (f,t,p)=>[f,t+" // EMERGENCY MEMO",["MEMO: Stop investigating "+t.toLowerCase()+".","STAFF: Why?","MEMO: Because "+p[2].toLowerCase(),"STAFF: This memo is making things worse."]],
  (f,t,p)=>[f,t+" // OBJECT TESTIMONY",["OBJECT: I would like to testify about "+t.toLowerCase()+".","STAFF: Proceed.","OBJECT: "+p[1],"STAFF: That explains absolutely nothing."]],
  (f,t,p)=>[f,t+" // BREAKING NEWS",["BREAKING: "+f+" has reported a "+t.toLowerCase()+" situation.","REPORTER: Is anyone concerned?","STAFF: "+p[3],"REPORTER: Excellent. I have more questions."]],
  (f,t,p)=>[f,t+" // MANAGEMENT MEETING",["MANAGEMENT: Agenda item one: "+t.toLowerCase()+".","STAFF: We already discussed this.","MANAGEMENT: Yes. The "+f+" version.","CHAIRPERSON: Meeting adjourned before it becomes worse."]]
 ];
 const out=[]; source.forEach(x=>modes.forEach(fn=>out.push(fn(x[0],x[1],x[2]))));
 window.HOSPITAL_CONTENT.facilityComics=out;
})();
