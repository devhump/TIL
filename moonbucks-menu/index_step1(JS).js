// 오늘 얻은 인사이트
// 1. 이벤트 위임을 어떻게 할 수 있는지 알게 되어서 좋았다.
// 2. 요구사항을 전략적으로 접근해야하는지, 단계별로 세세하게 나누는게 중요하다는 걸 알게 됐다.
// 3. DOM 요소를 가져올 때는 $ 표시를 써서 변수처럼 사용할 수 있는게 좋았다.
// 4. 새롭게 알게된 메서드 innerText, innerHTML, closest, insertAdjacentHtml, e.target
//

// ## step1 요구사항 - 돔 조작과 이벤트 핸들링으로 메뉴 관리하기
// TODO 메뉴추가
// - [X] 메뉴의 이름을 입력받고 엔터키 입력으로 추가한다.
// - [X] 메뉴의 이름을 입력받고 확인 버튼을 누르면 메뉴를 추가한다.
// - [X] 추가되는 메뉴의 아래 마크업은 `<ul id="espresso-menu-list" class="mt-3 pl-0"></ul>` 안에 삽입해야 한다.
// - [X] 총 메뉴 갯수를 count하여 상단에 보여준다.
// - [X] 메뉴가 추가되고 나면, input은 빈 값으로 초기화한다.
// - [X] 사용자 입력값이 빈 값이라면 추가되지 않는다.

// TODO 메뉴 수정
// - [X] 메뉴의 수정 버튼클릭 이벤트를 받고, 메뉴 이름을 수정하는 모달창(prompt)이 뜨다.
// - [X] 모달창에서 신규메뉴명을 입력 받고, 확인 버튼을 누르면 메뉴가 수정된다.

// TODO 메뉴 삭제
// - [X] 메뉴 삭제 버튼 클릭 이벤트를 받고, 메뉴 삭제 컨펌 모달창이 뜬다.
// - [X] 확인 버튼을 클릭하면 메뉴가 삭제된다.
// - [X] 총 메뉴 갯수를 count하여 상단에 보여준다.

const $ = (selector) => document.querySelector(selector);

function App() {
  const updateMenuCount = () => {
    // 메뉴 개수를 카운팅한다.
    const menuCount = $("#espresso-menu-list").querySelectorAll("li").length;
    $(".menu-count").innerText = `총 ${menuCount}개`;
  };

  const addMenuName = () => {
    if ($("#espresso-menu-name").value === "") {
      alert("값을 입력해주세요.");
      return;
    }
    const espressoMenuName = $("#espresso-menu-name").value;
    const menuItemTemplate = (espressoMenuName) => {
      return `
          <li class="menu-list-item d-flex items-center py-2">
        <span class="w-100 pl-2 menu-name">${espressoMenuName}</span>
        <button
          type="button"
          class="bg-gray-50 text-gray-500 text-sm mr-1 menu-edit-button"
        >
          수정
        </button>
        <button
          type="button"
          class="bg-gray-50 text-gray-500 text-sm menu-remove-button"
        >
          삭제
        </button>
      </li>`;
    };
    $("#espresso-menu-list").insertAdjacentHTML(
      "beforeend",
      menuItemTemplate(espressoMenuName)
    );

    updateMenuCount();

    // 메뉴 입력 받은 후 빈 값으로 초기화 한다
    $("#espresso-menu-name").value = "";
  };

  const updateMenuName = (e) => {
    const $menuName = e.target.closest("li").querySelector(".menu-name");
    const updatedMenuName = prompt("메뉴명을 수정하세요", $menuName.innerText);
    $menuName.innerText = updatedMenuName;
  };

  const removeMenuName = (e) => {
    e.target.closest("li").remove();
    updateMenuCount();
  };

  $("#espresso-menu-list").addEventListener("click", (e) => {
    if (e.target.classList.contains("menu-edit-button")) {
      updateMenuName(e);
    }

    if (e.target.classList.contains("menu-remove-button")) {
      if (confirm("정말 삭제하시겠습니까?")) {
        removeMenuName(e);
      }
    }
  });

  // form 태그가 자동으로 전송되는 걸 막아준다.
  $("#espresso-menu-form").addEventListener("submit", (e) => {
    e.preventDefault();
  });

  $("#espresso-menu-submit-button").addEventListener("click", addMenuName);

  // 메뉴의 이름을 입력받는다
  $("#espresso-menu-name").addEventListener("keypress", (e) => {
    if (e.key !== "Enter") {
      return;
    }
    addMenuName();
  });
}

App();
