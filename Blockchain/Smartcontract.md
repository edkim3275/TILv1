# smartcontract

## 1. 기초문법

```solidity
function FunctionName([parameters]) {public|private|internal|external} [pure|constant|view|payable] [modifiers] [returns (return types)]
```

- `FunctionName`

  각 컨트랙트마다 한 개의 함수는 이름이 없이 정의될 수 있는데, 이를 폴백(fallback) 함수라고 부른다. 다른 함수 이름이 없을 때 호출된다. 폴백 함수는 인수가 없으며 아무것도 반환할 수 없다.

- `parameters`

  이름 뒤에 함수 이름과 유형과 함께 전달되어야 하는 인수.

- ### 함수의 가시성(visibility)을 지정

  `public`

  기본값. 공개 함수는 **다른 컨트랙트 또는 EOA 트랜잭션 또는 컨트랙트 내에서 호출**할 수 있다.

  `external`

  외부 함수는 **명시적으로 키워드 `this`가 앞에 붙지 않는 한, 컨트랙트 내에서 호출할 수 없다**는 이점을 제외하면 공개 함수와 같다.

  `internal`

  내부 함수는 **컨트랙트 내에서만 접근**할 수 있다.

  다른 컨트랙트 또는 EOA 트랜잭션으로는 호출할 수 없다. 파생된 컨트랙트(이 컨트랙트를 상속받은 컨트랙트)에 의해서는 호출될 수 있다.

  `private`

  비공개 함수는 내부 함수와 유사하지만 파생된 컨트랙트에서도 호출할 수 없다.

- ### 함수의 동작에 영향

  `constant` 또는 `view`

  `view`로 표시된 함수는 상태를 변경하지 않는다. `constant`라는 용어는 향후 릴리스에서 사용되지 않는 뷰의 별칭

  오직 데이터를 읽을 수만 있고, 가스가 소모되지 않는다.

  `pure`

  순수 함수는 스토리지에서 변수를 읽거나 쓰지 않는 함수.

  `view`와 다르게 데이터를 읽는 것이 아니라 인자로 전달 받은 값을 활용해서 반환. (인자로 전달받은 값만을 활용한다.)

  가스가 소모 되지 않는다.

  ```solidity
  contract testContract {
  	uint student;
  	function isRight (uint a, uint b) public pure returns (uint) {
  		return a+b;
  	}
  }
  ```

  `payable`

  `payable`이 선언되어 있다면 입금을 받을 수 있는 함수. 그렇지 않다면 입금이 거부된다. (예외 : 보상지불 및 SELFDESTRUCT)

  함수 내에서 ETH 거래할 수 있게 한다.

  가스가 소모되지 않는다.

- ### 상태변수 타입 종류

  `uint`

  크기 : 8bit ~ 256bit. 크기를 선언하지 않은 uint는 uint256과 같다.

  int형보다 더 큰 범위의 정수를 선언할 수 있다.

  `address`

  20bytes로 크기가 고정되어 있는데 이는 이더리움 계정의 주소 크기에 맞게 설정되어 있는 것이다.

  address.balance와 address.transfer가 존재. balance는 주소가 보유한 이더의 양, transfer는 해당 주소에 이더를 보낼 수 있다.

  `bytes`

  크기 : 1byte ~ 32byte, 기본값 byte는 bytes1과 같다.

  가스 소모량은 동적 타입인 string이 bytes 형보다 크다. 따라서 정확한 크기를 알면 byte의 크기를 명시해주는 것이 가스 소모량을 줄이는데 효율적이다.

  `struct`

  필요한 자료형들을 가지고 새롭게 정의하는 사용자 정의 타입

  `mapping`

  mapping타입은 특정 key에 대한 value를 저장하거나 읽어오는데 유용하게 사용된다. 파이썬의 딕셔너리와 유사하다. ex) mapping(key => value)

  mapping 타입은 특정 key에 대한 값을 저장하고 조회하는 기능을 제공. 하지만 iterable한 key 목록을 반환해 주는 기능을 제공하지 않는다. iterable가능한 mapping을 만들고 싶으면 추가로 기능을 포함시켜야 한다.

  key 값은 동적 배열, 열거형, 구조체 매핑 타입을 제외한 다른 타입들은 모두 가능. value 값은 매핑 포함 다른 타입 모두 다 가능.

- ### Storage

  블록체인 상에 데이터가 저장되는 위치

  `storage`

  변수를 블록체인에 영구히 저장.

  상태변수는 기본적으로 storage로 선언

  `memory`

  컨트랙트가 종료되면 같이 사라짐

  임시로 변수를 저장하는 장소

  매개변수나 리턴값은 기본적으로 memory로 선언

- ### Interface

  추상함수와 같은 개념.(추상함수 : 구현이 이루어지지않고 단지 그 함수의 이름만 가지고 있다는 뜻)

  smartcontract는 본인만 사용하는 것이 아니라 다른 모든 사람들이 사용할 수 있기 때문에 어떠한 함수들을 사용할지 명시를 해주어서 일종의 '표준'을 만드는데. 이를 만들기 위해서 키워드 `interface`를 사용하게 된다.

  ```solidity
  interface ERC20Interface {
  	function totalSupply() external view returns (uint256); // 총발행량
  	function balanceOf(address account) external view returns (uint256); // 잔고. account가 가지고 있는 토큰의 수를 반환
  	function trasfer(address receiver, uint256 amount) external returns (bool); // 송금
  	function approve(address spender, uint256 amount) external returns (bool); // 승인. 토큰의 권한을 넘겨주는 함수
  	function allowance(address owner, address spender) external view returns (uint256); // 허용된 토큰의 개수
  	function trasferFrom(address spender, address receiver, uint256 amount) external returns (bool); // 유저간 송금
  	
  	// Transfer 이벤트는 transfer함수가 실행될때마다 로그를 남기고 Approval 이벤트는 approve 함수가 실행될 때 로그를 남긴다.
  	event Transfer(address indexed from, address indexed to, uint256 amount);
  	event Approval(address indexed owner, address indexed spender, uint256 oldamount, uint256 amount);
  }
  ```

- ### 에러처리

**assert, require, revert**

- 에러로 스마트 컨트랙트가 중지될 때는 둘 이상의 컨트랙트가 호출된 경우 컨트랙트 호출 연결을 따라 모든 상태(변수, 잔액 등의 변경)가 원래대로 되돌려진다.

- 통상적으로 `assert`는 결과가 참일 것으로 예상될 때 사용

- 이에 배해 `require`는 입력값(함수 파라미터 또는 트랜잭션 필드값)이 설정한 조건의 기댓값에 맞는지 테스트할 때 사용

  `require` 함수는 요구되는 조건이 만족되지 않을 경우 에러를 발생시켜 함수의 나머지 부분이 실행되지 않도록 하는 **게이트 조건(gate condition)** 기능을 한다.

  에러 메시지는 트랜잭션 로그로 기록된다.

  ```solidity
  require(msg.sender == owner, "Only the contract owner can call this function")
  ```

- `revert`와 `throw` 함수는 컨트랙트의 실행을 중지하고 모든 변경 상태를 되돌린다. (`throw` 함수는 더는 사용 x)

  `revert` 함수는 다른 변수 없이 에러 메시지만을 인수로 사용할 수도 있고, 이 메시지는 트랜잭션 로그에 기록된다.

  ```solidity
  // 조건이 충족되지않다면 알아서 transfer 함수가 에러를 낼 것.
  msg.sender.transfer(withdraw_amount);
  
  // 추가적인 에러 검사코드로 보다 나은 에러 리포팅을 얻을 수 있다.
  require(this.balance >= withdraw_amount, "Insufficient balance in faucet for withdrawal request");
  msg.sender.transfer(withdraw_amount);
  ```

- ### 이벤트

트랜잭션 영수증(transaction receipt)에 있는 로그들을 만들기 위해 사용되는 객체.

- 특정한 이벤트가 일어나는지 '감시(watch)'해서 사용자 인터페이스에 반영하거나, 해당 컨트랙트상의이벤트에 대응되는 변화를 애플리케이션의 상태에도 반영되도록 할 수 있다.

- 이벤트 객체는 인수들을 취할 수 있다. 이는 시리얼라이즈되어서 블록체인상의 트랜잭션 로그에 기록된다. 인수 앞에 `indexed`라는 키워드를 붙여서 애플리케이션에서 검색하거나 필터링할 수 있는, 인덱싱된 테이블(해시 테이블)의 값으로 만들 수 있다.

  ```solidity
  contract Faucet is mortal {
  	// 출금(Withdrawal)
  	event Withdrawal(address indexed to, uint amount);
  	// 입금(Deposit)
  	event Deposit(address indexed from, uint amount);
  	
  	function withdraw(uint withdraw_amount) public {
  		msg.sender.transfer(withdraw_amount);
  		emit Withdrawal(msg.sender, withdraw_amount);
  	}
  	
  	function () public payable {
  		emit Deposit(msg.sender, msg.value)
  	}
  }
  ```

- 이벤트 받기(catch)는 어떻게 할까? web3.js 라이브러리는 트랜잭션의 로그를 포함하는 데이터 구조를 제공한다. 그 로그를 통해 트랜잭션에 의해 생성된 이벤트를 볼 수 있다.

## 2. PancakeSwap의 경우

PancakeSwap Exchange(Factory, Router), MasterChef, CAKE Syrup Pool, Prediction V2, Lottery v2

### Main staking contract/MasterChef

### MasterChef

링크 : https://bscscan.com/address/0xa5f8C5Dbd5F286960b9d90548680aE5ebFf07652#code

MasterChef is the master of Cake. He can make Cake and he is a fair guy.

```solidity
contract MasterChefV2 is Ownable, ReentrancyGuard {
	// Deposits a dummy token to `MASTER_CHEF` MCV1. This is required because MCV1 holds the minting permission on CAKE.
	function init(IBEP20 dummyToken) external onlyOwner {}
	
	// Returns the number of MCV2 pools
	function poolLength() public view returns(uint256 pools) {}
	
	// add a new pool. can only be called by the owner.
	// @param _allocPoint Number of allocation points for the new pool
	// @param _lpToken Address of the LP BEP-20 token
	// @param _isRegular Whether the pool is regular or special. LP farms are always "regular". "special" pools are only for CAKE distributions within PancakeSwap products
	// @param _withUpdate Whether call "massUpdatePools" operation
	function add(
		uint256 _allocPoint,
		IBEP20 _lpToken,
		bool _isRegular,
		bool _withUpdate
	) external onlyOwner {}
	
	// update the given pool's CAKE allocation point. can only called by the owner.
	// @param _pid The id of the pool. See `poolInfo`
	// @param _allocPoint New number of allocation points for the pool
	// @param _withUpdate Whether call "massUpdatePools" operation
	function set(
		uint256 _pid,
		uint256 _allocPoint,
		bool _withUpdate
	) external onlyOwner {}
	
	// View function for checking pending CAKE rewards
	// @param _user Address of the user
	function pendingCake(uint256 _pid, address _user) external view returns (uint256) {}
	
	// Update cake reward for all the active pools. Be careful of gas spending!
	function massUpdatePools() public {}
	
	// Calculates and returns the `amount` of CAKE per block
	// @param _isRegular If the pool belongs to regular or special
    function cakePerBlock(bool _isRegular) public view returns (uint256 amount) {}
    
    // Update reward variables for the given pool.
    // @return pool Returns the pool that was updated
    function updatePool(uint256 _pid) public returns (PoolInfo memory pool) {}
    
    // Deposit LP tokens to pool
    function deposit(uint256 _pid, uint256 _amount) external nonReentrant {}
    
    // Withdraw LP tokens from pool
    function withdraw(uint256 _pid, uint256 _amount) external nonReentrant {}
    
    // Harvest CAKE from `MASTER_CHEF` MCV1 and pool `MASTER_PID` to MCV2
    function harvestFromMasterChef() public {}
    
    // Withdraw without caring about the rewards. EMERGENCY ONLY.
    function emergencyWithdraw(uint256 _pid) public onlyOwner {}
    
    // Send CAKE pending for burn to `burnAdmin`
    function burnCake(bool _withUpdate) public onlyOwner {}
    
    // Update the % of CAKE distributions for burn, regular pools and special pools
    function updateCakeRate(
    	uint256 _burnRate,
    	uint256 _regularFarmRate,
    	uint256 _specialFarmRate,
    	bool _withUpdate
    ) external onlyOwner {}
    
    // Update Whitelisted addresses for special pools
    function updateWhiteList(address _user, bool _isValid) external onlyOwner {}
    
    // Update boost contract address and max boost factor
    function updateBoostContract(address _newBoostContract) external onlyOwner {}
    
    // Update user boost factor
    function updateBoostMultiplier(
    	address _user,
    	uint256 _pid,
    	uint256 _newMultiplier
    ) external onlyBoostContract nonReentrant {}
    
    // Get user boost multiplier for specific pool id
    function getBoostMultiplier(address _user, uint256 _pid) public view returns (uint256) {}
    
    // Settles, distribute the pending CAKE rewards for given user.
    function settlePendingCake(
    	address _user,
    	uint256 _pid,
    	uint256 _boostMultiplier
    ) internal {}
    
    // Safe Transfer CAKE
    // @param _to The CAKE receiver address
    function _safeTransfer(address _to, uint256 _amount) internal {}
}
```



### PancakeSwap Exchange

#### Factory v2

링크 : https://github.com/pancakeswap/pancake-swap-core/blob/master/contracts/PancakeFactory.sol

```solidity
interface IPancakeFactory {
	// Emitted whenever a createPair creates a new pai
    event PairCreated(address indexed token0, address indexed token1, address pair, uint);
	
	// The address to where non-LP-holder fees are sent
    function feeTo() external view returns (address);
    // The address with permission to set the feeTo address
    function feeToSetter() external view returns (address);
	// Address for tokenA and address for tokenB return address of pair contract
    function getPair(address tokenA, address tokenB) external view returns (address pair);
    // Returns the address of the nth pair created through the Factory contract
    function allPairs(uint) external view returns (address pair);
    // Displays the current number of pairs created through the Factory contract as an integer
    function allPairsLength() external view returns (uint);
    
	// Creates a pair for tokenA and tokenB where a pair doesn't already exist
    function createPair(address tokenA, address tokenB) external returns (address pair);
	// Set address for feeTo
    function setFeeTo(address) external;
    // Sets address for permission to adjust feeTo
    function setFeeToSetter(address) external;
}

contract PancakeERC20 is IPancakeERC20 {}
contract PancakePair is IPancakePair, IPancakeERC20 {}
contract PancakeFactory is IPancakeFactory {}
```



#### Router v2

**Read functions**

- `WETH` : Returns the canonical address for Binance : WBNB token
- `factory` : Returns the canonical address for PancakeFactory
- `getAmountOut`, `getAmountIn`, `getAmountsOut`, `getAmountsIn`, `quote`

**Write functions**

- `addLiquidity` : Adds liquidity to a BEP20⇄BEP20 pool
- `addLiquidityETH` : Adds liquidity to a BEP20⇄WBNB pool
- `removeLiquidity` : Removes liquidity from a BEP20⇄BEP20 pool
- `removeLiquidityETH` : Removes liquidity from a BEP20⇄WBNB pool
- `removeLiquidityETHSupportingFeeOnTransferTokens` : Removes liquidity from BEP20⇄ WBNB for tokens that takes a fee on transfer
- `removeLiquidityETHWithPermit` : Removes liquidity from a BEP20⇄WBNB and receives BNB, without pre-approval, via permit.
- `swapETHForExactTokens` : Receive an exact amount of output tokens for as little BNB as possible.(가능한 한 적은 BNB로 정확한 양의 출력 토큰을 받습니다.)
- `swapExactETHForTokens` : Receive as many output tokens as possible for an exact amount of BNB.(정확한 양의 BNB에 대해 가능한 한 많은 출력 토큰을 받습니다.)
- `swapExactETHForTokensSupportingFeeOnTransferTokens` : Receive as many output tokens as possible for an exact amount of BNB. Supports tokens that take a fee on transfer.(정확한 양의 BNB에 대해 가능한 한 많은 출력 토큰을 받습니다. 전송 시 수수료를 받는 토큰을 지원합니다.)
- `swapExactTokensForETH` : Receive as much BNB as possible for an exact amount of input tokens.(정확한 양의 입력 토큰에 대해 최대한 많은 BNB를 받습니다.)
- `swapExactTokensForETHSupportingFeeOnTransferTokens` : Receive as much BNB as possible for an exact amount of tokens. Supports tokens that take a fee on transfer.(정확한 양의 토큰에 대해 가능한 한 많은 BNB를 받으십시오. 전송 시 수수료를 받는 토큰을 지원합니다.)
- `swapExactTokensForTokens` : Receive as many output tokens as possible for an exact amount of input tokens.(정확한 양의 입력 토큰에 대해 가능한 한 많은 출력 토큰을 받습니다.)

## 3. 적용

### 민팅사례

- pancakeSwap

```js
function mint(address to) external lock returns (uint liquidity) {
    (uint112 _reserve0, uint112 _reserve1) = getReserves(); // gas savings
    uint balance0 = IERC20(token0).balanceOf(address(this));
    uint balance1 = IERC20(token1).balanceOf(address(this));
    uint amount0 = balance0.sub(_reserve0);
    uint amount1 = balance1.sub(_reserve1);
    
    bool feeOn = _mintFee(_reserve0, _reserve1);
    uint _totalSupply = totalSupply; // gas savings, must be defined here since totalSupply can update in _mintFee
    if (_totalSupply == 0) {
        liquidity = Math.sqrt(amount0.mul(amount1)).sub(MINIMUM_LIQUIDITY);
        _mint(address(0), MINIMUM_LIQUIDITY); // permanently lock the first MUNIMUM_LIQUIDITY tokens
    } else {
        liquidity = Math.min(amount0.mul(_totalSupply) / _reserve0, amount1.mul(_totalSupply) / reserve1);
    }
    require(liquidity > 0, 'Pancake: INSUFFICIENT_LIQUIDITY_MINTED');
    _mint(to, liquidity);
    
    _update(balance0, balance1, _reserve0, _reserve1);
    if (feeOn) kLast = uint(reserve0).mul(reserve1); // reserve0 and reserve1 are up-to-date
    emit Mint(msg.sender, amount0, amount1);
}
```

-  ERC721

```js
pragma solidity 0.8.0;
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";

contract MintProdToken is ERC721Enumerable {
	constructor() ERC721("Meta", "Symbol") {}
    
    // 계약서에 포함된 토큰의 속성들을 구조체로 정의
    struct ProdTokenData {
        uint256 prodTokenId;
        string serialNo;
        string productType;
        addrses lastOwner;
        uint256 lastPrice;
        uint256 price;
        uint256 repairedCount;
    }
    
    mapping(uint256 => string) serialNo;
    mapping(uint256 => string) productType;
    mapping(uint256 => address) lastOwner;
    mapping(uint256 => uint256) lastPrice;
    mapping(uint256 => uint256) price;
    mapping(uint256 => uint256) repairedCount;
    
    function mintProdToken(string memory _serialNo, string memory _productType, uint256 _price) public {
        uint256 prodTokenId = totalSupply() + 1;
        
        serialNo[prodTokenId] = _serialNo;
        productType[prodTokenId] = _productType;
        lastOwner[prodTokenId] = msg.sender;
        lastPrice[prodTokenId] = _price;
        price[prodTokenId] = _price;
        repairedCount[prodTokenId] = 0;
        
        _mint(msg.sender, prodTokenId);
    }
    
    function getProdToken(address _prodTokenOwner) view public returns (ProdTokenData[] memory) {
        uint256 length = balanceOf(_prodTokenOwner);
        
        require(length != 0, "No Purchased Item");
        
        ProdTokenData[] memory prodTokenData = new ProdTokenData[](length);
        
        for (uint i=0; i<length; i++) {
            uint256 prodTokenId = tokenOfOwnerByIndex(_prodTokenOwner, i);
            string memory _serialNo = serialNo[prodTokenId];
            string memory _productType = productType[prodTokenId];
            address _lastOnwer = lastOwner[prodTokenId];
            uint256 _lastPrice = lastPrice[prodTokenId];
            uint256 _price = price[prodTokenId];
            uint256 _repairedCount = repairedCount[prodTokenId];
            
            prodTokenData[i] = ProdTokenData(prodTokenId, _serialNo, _productType, _lastOnwer, _lastPrice, _price, _repairedCount);
        }
        
        return prodTokenData;
    }
```

### 스컨 필요 함수

- Master(TMB)

```solidity
contract TmaxMetaBank is Ownable {
	
}
```



- Ownable

```solidity
import "./Context.sol";
contract Ownable is Context {
	address private _owner;
	
	constructor () internal {
		address msgSender = _msgSender();
		_owner = msgSender;
	}
	
	// Returns the address of the owner.
	function owner() public view returns (address) {
		return _owner;
	}
	
	modifier onlyOwner() {
		require(_owner == _msgSender(), "Ownable: caller is not the owner.");
		_;
	}
}
```



- Context : Provides information about the current execution context, including the sender of the tx and its data

```solidity
abstract contract Context {
	function _msgSender() internal view virtual returns (address payable) {
		return msg.sender;
	}
	
	function _msgData() internal view virtual returns (bytes memory) {
		this;
		return msg.data;
	}
}
```



- ReentrancyGuard : Contract module that helps prevent reentrant calls to a function

```solidity
contract ReentrancyGuard {
	uint256 private constant _NOT_ENTERED = 1;
	uint256 private constant _ENTERED = 2;
	
	uint256 private _status;
	
	constructor () internal {
		_status = _NOT_ENTERED;
	}
	
	modifier nonReentrant() {
		// 첫 호출에는 _notentered가 true(따라서 require문 통과한다.)
		require(_status != _ENTERED, "ReentrancyGuard: reentrant call");
		
		// _entered가 true가 되면서 이후 호출은 모두 에러메시지가 발생한다.
		_status = _ENTERED;
		
		_;
		
		// By storing the original value once again, a refund is triggered.
		_status = _NOT_ENTERED;
	}
}
```



- ERC20

```solidity
abstract contract Context {
    function _msgSender() internal view virtual returns (address payable) {
        return msg.sender;
    }

    function _msgData() internal view virtual returns (bytes memory) {
        this;
        return msg.data;
    }
}

contract ERC20 is Context, IERC20, IERC20Metadata {
    mapping(address => uint256) private _balances;

    mapping(address => mapping(address => uint256)) private _allowances;

    uint256 private _totalSupply;

    string private _name;
    string private _symbol;
    
    constructor(string memory name_, string memory symbol_) {
        _name = name_;
        _symbol = symbol_;
    }
	
	function name() public view virtual override returns (string memory) {
        return _name;
    }
    
    function symbol() public view virtual override returns (string memory) {
        return _symbol;
    }
    
    function decimals() public view virtual override returns (uint8) {
        return 18;
    }
    
    function totalSupply() public view virtual override returns (uint256) {
        return _totalSupply;
    }

    function balanceOf(address account) public view virtual override returns (uint256) {
        return _balances[account];
    }
    
    function transfer(address to, uint256 amount) public virtual override returns (bool) {
        address owner = _msgSender();
        _transfer(owner, to, amount);
        return true;
    }
    
    function allowance(address owner, address spender) public view virtual override returns (uint256) {
        return _allowances[owner][spender];
    }

    function approve(address spender, uint256 amount) public virtual override returns (bool) {
        address owner = _msgSender();
        _approve(owner, spender, amount);
        return true;
    }
    
    function transferFrom(
        address from,
        address to,
        uint256 amount
    ) public virtual override returns (bool) {
        address spender = _msgSender();
        _spendAllowance(from, spender, amount);
        _transfer(from, to, amount);
        return true;
    }
    
    function increaseAllowance(address spender, uint256 addedValue) public virtual returns (bool) {
        address owner = _msgSender();
        _approve(owner, spender, allowance(owner, spender) + addedValue);
        return true;
    }
    
    function decreaseAllowance(address spender, uint256 subtractedValue) public virtual returns (bool) {
        address owner = _msgSender();
        uint256 currentAllowance = allowance(owner, spender);
        require(currentAllowance >= subtractedValue, "ERC20: decreased allowance below zero");
        unchecked {
            _approve(owner, spender, currentAllowance - subtractedValue);
        }

        return true;
    }
    
    function _transfer(address spender, address recipient, uint amount) internal {
        require(from != address(0), "ERC20: transfer from the zero address");
        require(to != address(0), "ERC20: transfer to the zero address");

        _beforeTokenTransfer(from, to, amount);

        uint256 fromBalance = _balances[from];
        require(fromBalance >= amount, "ERC20: transfer amount exceeds balance");
        unchecked {
            _balances[from] = fromBalance - amount;
        }
        _balances[to] += amount;

        emit Transfer(from, to, amount);

        _afterTokenTransfer(from, to, amount);
    }

	function _mint(address account, uint256 amount) internal virtual {
        require(account != address(0), "ERC20: mint to the zero address");

        _beforeTokenTransfer(address(0), account, amount);

        _totalSupply += amount;
        _balances[account] += amount;
        emit Transfer(address(0), account, amount);

        _afterTokenTransfer(address(0), account, amount);
    }
    
    function _burn(address account, uint256 amount) internal virtual {
        require(account != address(0), "ERC20: burn from the zero address");

        _beforeTokenTransfer(account, address(0), amount);

        uint256 accountBalance = _balances[account];
        require(accountBalance >= amount, "ERC20: burn amount exceeds balance");
        unchecked {
            _balances[account] = accountBalance - amount;
        }
        _totalSupply -= amount;

        emit Transfer(account, address(0), amount);

        _afterTokenTransfer(account, address(0), amount);
    }
	
	function _approve(
        address owner,
        address spender,
        uint256 amount
    ) internal virtual {
        require(owner != address(0), "ERC20: approve from the zero address");
        require(spender != address(0), "ERC20: approve to the zero address");

        _allowances[owner][spender] = amount;
        emit Approval(owner, spender, amount);
    }
    
    function _spendAllowance(
        address owner,
        address spender,
        uint256 amount
    ) internal virtual {
        uint256 currentAllowance = allowance(owner, spender);
        if (currentAllowance != type(uint256).max) {
            require(currentAllowance >= amount, "ERC20: insufficient allowance");
            unchecked {
                _approve(owner, spender, currentAllowance - amount);
            }
        }
    }
    
    function _beforeTokenTransfer(address from, address to, uint256 amount) internal virtual {}

	function _afterTokenTransfer(address from, address to, uint256 amount) internal virtual {}
}




```



## 참고링크

pancake-smart-contracts 깃헙 : https://github.com/pancakeswap/pancake-smart-contracts

스마트 컨트랙트와 ERC-20개발 : https://velog.io/@yonaaaaaaa_a/%EC%8A%A4%EB%A7%88%ED%8A%B8-%EC%BB%A8%ED%8A%B8%EB%9E%99%ED%8A%B8%EC%99%80-ERC-20-%EA%B0%9C%EB%B0%9C

스마트 컨트랙트 소개 : https://solidity-kr.readthedocs.io/ko/latest/introduction-to-smart-contracts.html#blockchain-basics

스마트 컨트랙트 개발 주의사항 : https://medium.com/rayonprotocol/%EC%9D%B4%EB%8D%94%EB%A6%AC%EC%9B%80-%EC%8A%A4%EB%A7%88%ED%8A%B8-%EC%BB%A8%ED%8A%B8%EB%9E%99%ED%8A%B8-%EA%B0%9C%EB%B0%9C-%EC%A3%BC%EC%9D%98%EC%82%AC%ED%95%AD-5a1abde1a4e0

## 용어정리

- BEP20 : ERC-20의 확장. Binance 플랫폼 스마트 체인의 토큰 표준.

- WBNB : Wrapped BNB. 바이낸스토큰(BNB)을 디파이에서 활용하기 위해 전환된 토큰.

- 러그풀사건 : NFT를 팔아 투자금을 모은 뒤 도주하는 행위

- 스마트컨트랙트 함수 실행

  배포를 하면서 얻게된 abi를 contract object상에 넣고 instance를 생성 ➭ instance상에 스마트컨트랙스 상의 함수가 메서드로 존재하게된다. ➭ instance.method.methodName() 이런식으로 스마트컨트랙트 함수를 실행(아래의 과정을 대신해주는 것)

  - method를 16진수로 인코드 ➭ tx의 data로 넣어서 tx전송 ➭ EVM이 tx을 받으면서 data field의 16진수를 읽음 ➭ 16진수를 다시 opcode로 변환

- 에어드랍 : 특정 암호화폐를 보유한 사람에게 어떤 비율로 다른 암호화폐를 지급하는 것. 투자 비율에 따라 해당 코인/토큰을 무료로 커뮤니티에 지급하는 것.

- address(0) : 새 계약이 배포되고 있음을 나타내는데 사용되는 특별한 경우. 트랜잭션의 새 계약. 주소가 0인 계정의 경우 트랜잭션은 새 계약을 작성한다. '0x0'은 원시 트랜잭션의 to 필드로 설정된다.

  ```solidity
  transaction = {
    nonce: '0x0', 
    gasLimit: '0x6acfc0', // 7000000
    gasPrice: '0x4a817c800', // 20000000000
    to: '0x0',
    value: '0x0',
    data: '0xfffff'
  };
  ```

  

