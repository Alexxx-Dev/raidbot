# -*- coding: utf8 -*-
import time

import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.keyboard import VkKeyboard


vk = vk_api.VkApi(token='TOKEN')
longpoll = VkBotLongPoll(vk, GROUP_ID)
vk = vk.get_api()


msg = "GG ACTIVATE!\n0&#8419; 1&#8419; 2&#8419; 3&#8419; 4&#8419; 5&#8419; 6&#8419; 7&#8419; 8&#8419; 9&#8419; &#153; &#8252; &#8265; &#8482; &#8505; &#8596; &#8597; &#8598; &#8599; &#8600; &#8601; &#8617; &#8618; &#8987; &#8986; &#9193; &#9194; &#9195; &#9196; &#9200; &#9203; &#9410; &#9642; &#9643; &#9654; &#9664; &#9723; &#9724; &#9725; &#9726; &#9728; &#9729; &#9745; &#9749; &#9748; &#9742; &#9757; &#9786; &#9800; &#9801; &#9802; &#9803; &#9804; &#9805; &#9807; &#9806; &#9808; &#9809; &#9810; &#9811; &#9824; &#9829; &#9827; &#9830; &#9832; &#9851; &#9855; &#9875; &#9888; &#9889; &#9899; &#9898; &#9917; &#9918; &#9925; &#9924; &#9934; &#9940; &#9962; &#9971; &#9970; &#9973; &#9978; &#9981; &#9986; &#9989; &#9995; &#9994; &#9993; &#9992; &#9996; &#9999; &#10002; &#10004; &#10006; &#10024; &#10035; &#10036; &#10052; &#10055; &#10060; &#10062; &#10067; &#10068; &#10069; &#10071; &#10084; &#10133; &#10135; &#10134; &#10145; &#10160; &#10175; &#10548; &#10549; &#11013; &#11015; &#11014; &#11035; &#11036; &#11088; &#11093; &#12336; &#12349; &#126980; &#127183; &#127344; &#127345; &#127358; &#127359; &#127374; &#127377; &#127379; &#127381; &#127380; &#127378; &#127382; &#127383; &#127384; &#127386; &#127385; &#127489; &#127744; &#127748; &#127745; &#127747; &#127746; &#127749; &#127750; &#127752; &#127751; &#127753; &#127754; &#127755; &#127756; &#127758; &#127757; &#127759; &#127761; &#127760; &#127762; &#127763; &#127764; &#127765; &#127766; &#127767; &#127768; &#127769; &#127770; &#127771; &#127772; &#127773; &#127775; &#127774; &#127776; &#127792; &#127793; &#127794; &#127795; &#127796; &#127797; &#127800; &#127801; &#127802; &#127799; &#127803; &#127804; &#127805; &#127806; &#127807; &#127808; &#127809; &#127810; &#127812; &#127813; &#127811; &#127814; &#127815; &#127816; &#127817; &#127818; &#127819; &#127820; &#127821; &#127822; &#127823; &#127825; &#127827; &#127826; &#127824; &#127829; &#127828; &#127830; &#127831; &#127832; &#127833; &#127835; &#127834; &#127838; &#127836; &#127837; &#127839; &#127840; &#127843; &#127841; &#127846; &#127845; &#127842; &#127844; &#127849; &#127847; &#127850; &#127848; &#127851; &#127852; &#127854; &#127853; &#127855; &#127856; &#127857; &#127858; &#127859; &#127860; &#127862; &#127863; &#127861; &#127864; &#127866; &#127865; &#127868; &#127867; &#127873; &#127872; &#127874; &#127875; &#127876; &#127877; &#127879; &#127878; &#127880; &#127881; &#127882; &#127884; &#127883; &#127885; &#127887; &#127886; &#127888; &#127889; &#127890; &#127891; &#127906; &#127905; &#127904; &#127907; &#127909; &#127908; &#127910; &#127912; &#127911; &#127913; &#127915; &#127914; &#127917; &#127916; &#127920; &#127918; &#127919; &#127921; &#127922; &#127924; &#127923; &#127925; &#127926; &#127929; &#127928; &#127930; &#127927; &#127931; &#127932; &#127933; &#127934; &#127935; &#127936; &#127937; &#127938; &#127939; &#127940; &#127942; &#127943; &#127944; &#127945; &#127946; &#127968; &#127969; &#127971; &#127970; &#127972; &#127973; &#127975; &#127974; &#127976; &#127977; &#127978; &#127979; &#127981; &#127982; &#127980; &#127984; &#127983; &#128000; &#128001; &#128002; &#128004; &#128003; &#128005; &#128006; &#128007; &#128009; &#128008; &#128010; &#128013; &#128014; &#128012; &#128011; &#128015; &#128016; &#128017; &#128020; &#128018; &#128021; &#128019; &#128023; &#128022; &#128024; &#128025; &#128026; &#128027; &#128029; &#128028; &#128030; &#128031; &#128032; &#128033; &#128034; &#128036; &#128037; &#128038; &#128039; &#128041; &#128035; &#128040; &#128042; &#128043; &#128044; &#128045; &#128047; &#128049; &#128046; &#128050; &#128048; &#128051; &#128053; &#128055; &#128054; &#128052; &#128056; &#128057; &#128059; &#128060; &#128058; &#128061; &#128062; &#128064; &#128066; &#128068; &#128067; &#128069; &#128070; &#128071; &#128072; &#128073; &#128074; &#128076; &#128078; &#128075; &#128077; &#128079; &#128080; &#128081; &#128083; &#128084; &#128082; &#128086; &#128085; &#128087; &#128088; &#128089; &#128090; &#128091; &#128092; &#128093; &#128095; &#128094; &#128096; &#128097; &#128098; &#128099; &#128100; &#128101; &#128103; &#128102; &#128104; &#128105; &#128107; &#128106; &#128108; &#128109; &#128110; &#128111; &#128113; &#128112; &#128114; &#128115; &#128116; &#128117; &#128120; &#128119; &#128118; &#128122; &#128121; &#128123; &#128125; &#128124; &#128127; &#128126; &#128129; &#128128; &#128130; &#128131; &#128132; &#128134; &#128133; &#128135; &#128136; &#128138; &#128139; &#128137; &#128141; &#128140; &#128143; &#128144; &#128142; &#128145; &#128146; &#128147; &#128148; &#128149; &#128150; &#128151; &#128152; &#128153; &#128154; &#128155; &#128156; &#128157; &#128158; &#128160; &#128159; &#128161; &#128162; &#128163; &#128164; &#128165; &#128167; &#128166; &#128169; &#128168; &#128170; &#128171; &#128173; &#128172; &#128174; &#128175; &#128177; &#128176; &#128178; &#128179; &#128180; &#128182; &#128184; &#128181; &#128185; &#128183; &#128186; &#128190; &#128189; &#128187; &#128188; &#128192; &#128191; &#128193; &#128195; &#128196; &#128198; &#128194; &#128197; &#128200; &#128199; &#128203; &#128205; &#128201; &#128202; &#128204; &#128206; &#128207; &#128208; &#128210; &#128209; &#128213; &#128212; &#128211; &#128214; &#128215; &#128217; &#128218; &#128219; &#128221; &#128216; &#128222; &#128220; &#128224; &#128223; &#128225; &#128226; &#128228; &#128227; &#128230; &#128232; &#128231; &#128229; &#128233; &#128234; &#128236; &#128237; &#128235; &#128238; &#128239; &#128240; &#128242; &#128244; &#128241; &#128245; &#128247; &#128246; &#128249; &#128252; &#128250; &#128251; &#128258; &#128257; &#128256; &#128260; &#128259; &#128261; &#128263; &#128264; &#128262; &#128266; &#128267; &#128265; &#128243; &#128268; &#128269; &#128270; &#128274; &#128271; &#128272; &#128273; &#128277; &#128275; &#128278; &#128276; &#128279; &#128280; &#128283; &#128281; &#128282; &#128284; &#128286; &#128285; &#128287; &#128289; &#128290; &#128293; &#128288; &#128291; &#128292; &#128295; &#128296; &#128294; &#128298; &#128297; &#128299; &#128301; &#128302; &#128300; &#128303; &#128304; &#128305; &#128307; &#128309; &#128308; &#128306; &#128310; &#128312; &#128314; &#128313; &#128311; &#128315; &#128316; &#128317; &#128507; &#128509; &#128510; &#128511; &#128512; &#128508; &#128513; &#128514; &#128515; &#128516; &#128517; &#128519; &#128520; &#128518; &#128521; &#128523; &#128522; &#128524; &#128525; &#128527; &#128529; &#128526; &#128528; &#128530; &#128531; &#128532; &#128535; &#128533; &#128536; &#128534; &#128537; &#128538; &#128540; &#128539; &#128541; &#128543; &#128544; &#128542; &#128545; &#128547; &#128548; &#128549; &#128546; &#128550; &#128551; &#128553; &#128552; &#128554; &#128555; &#128556; &#128557; &#128558; &#128561; &#128560; &#128559; &#128562; &#128565; &#128567; &#128563; &#128566; &#128569; &#128572; &#128571; &#128570; &#128574; &#128575; &#128564; &#128573; &#128576; &#128568; &#128581; &#128584; &#128586; &#128582; &#128583; &#128585; &#128587; &#128591; &#128590; &#128589; &#128588; &#128641; &#128640; &#128642; &#128644; &#128643; &#128645; &#128647; &#128646; &#128648; &#128649; &#128650; &#128651; &#128652; &#128654; &#128653; &#128655; &#128656; &#128658; &#128657; &#128659; &#128660; &#128662; &#128663; &#128661; &#128666; &#128664; &#128665; &#128669; &#128668; &#128667; &#128670; &#128672; &#128671; &#128674; &#128675; &#128673; &#128676; &#128677; &#128678; &#128679; &#128680; &#128681; &#128682; &#128684; &#128685; &#128683; &#128687; &#128686; &#128688; &#128689; &#128692; &#128693; &#128690; &#128694; &#128695; &#128691; &#128698; &#128697; &#128699; &#128700; &#128696; &#128701; &#128702; &#128703; &#128706; &#128704; &#128705; &#128709; &#128708; &#128707; &#127464;&#127475; &#127465;&#127466; &#127466;&#127480; &#127467;&#127479; &#127468;&#127463; &#127470;&#127481; &#127471;&#127477; &#127472;&#127479; &#127479;&#127482; &#127482;&#127480;"


menu = VkKeyboard()
menu.add_button(
    label=f"STOP!{' '*22}vto.pe",
    color="positive"
)
menu.add_button(
    label=f"STOP!{' '*22}vto.pe",
    color="negative"
)

menu.add_line()
menu.add_button(
                label=f"STOP!{' '*22}vto.pe",
                color="primary")

menu.add_button(
                label=f"STOP!{' '*22}vto.pe",
                color="positive")

menu = menu.get_keyboard()


for event in longpoll.listen():
    if event.type == VkBotEventType.MESSAGE_NEW:
        if event["from_id"] == 544332520:
            
            if event.object.message["text"].lower() == "/gg":
                try:
                    time.sleep(2)
                    vk.messages.send(
                        peer_id=event.object.message["peer_id"],
                        message=msg,
                        keyboard=menu,
                        random_id=0
                    )

                except Exception as e:
                    time.sleep(5)
                    continue

            if event.object.message["text"].lower() == "/stop":
                vk.messages.send(
                    peer_id=event.object.message["peer_id"],
                    message="[Process finished]",
                    keyboard=menu,
                    random_id=0
                )
