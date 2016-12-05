# coding: utf-8
from sqlalchemy import Column, Date, DateTime, Float, ForeignKey, Integer, Numeric, String, Table, Text, text
from sqlalchemy.dialects.mysql.types import BIT
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


t_chassis = Table(
    'chassis', metadata,
    Column('ProductID', ForeignKey('product.ProductID'), nullable=False, index=True),
    Column('type', Text),
    Column('atx', BIT(1)),
    Column('miniAtx', BIT(1)),
    Column('miniItx', BIT(1)),
    Column('fans', Text),
    Column('brand', Text),
    Column('height', Text),
    Column('width', Text),
    Column('depth', Text),
    Column('weight', Text)
)


class Con(Base):
    __tablename__ = 'cons'

    ReviewID = Column(ForeignKey('review.ReviewID'), nullable=False, index=True)
    ID = Column(Integer, primary_key=True)
    fact = Column(Text, nullable=False)

    review = relationship('Review')

# t_cpu
Cpu = Table(
    'cpu', metadata,
    Column('ProductID', ForeignKey('product.ProductID'), nullable=False, index=True),
    Column('model', Text),
    Column('clock', Text),
    Column('maxTurbo', Text),
    Column('integratedGpu', Text),
    Column('stockCooler', BIT(1)),
    Column('manufacturer', Text),
    Column('cpuSeries', Text),
    Column('logicalCores', Integer),
    Column('physicalCores', Integer),
    Column('socket', Text)
)


class Crawlprogres(Base):
    __tablename__ = 'crawlprogress'

    Site = Column(String(255), primary_key=True)
    Queue = Column(String)
    date = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


t_gpu = Table(
    'gpu', metadata,
    Column('ProductID', ForeignKey('product.ProductID'), nullable=False, index=True),
    Column('processorManufacturer', Text),
    Column('chipset', Text),
    Column('graphicsProcessor', String(255)),
    Column('architecture', Text),
    Column('cooling', Text),
    Column('memSize', Text),
    Column('pciSlots', Integer),
    Column('manufacturer', Text),
    Column('clock', Text),
    Column('boostedClock', Text),
    Column('model', Text)
)


t_harddrive = Table(
    'harddrive', metadata,
    Column('ProductID', ForeignKey('product.ProductID'), nullable=False, index=True),
    Column('isInternal', BIT(1)),
    Column('type', Text),
    Column('formFactor', Text),
    Column('capacity', Text),
    Column('cacheSize', Text),
    Column('transferRate', Text),
    Column('brand', Text),
    Column('sata', Text),
    Column('height', Text),
    Column('depth', Text),
    Column('width', Text)
)


t_motherboard = Table(
    'motherboard', metadata,
    Column('ProductID', ForeignKey('product.ProductID'), nullable=False, index=True),
    Column('formFactor', Text),
    Column('cpuType', Text),
    Column('cpuCount', Integer),
    Column('socket', Text),
    Column('netCard', BIT(1)),
    Column('soundCard', BIT(1)),
    Column('multiGPU', BIT(1)),
    Column('crossfire', BIT(1)),
    Column('sli', BIT(1)),
    Column('maxMem', Integer),
    Column('memSlots', Integer),
    Column('memType', Text),
    Column('graphicsCard', BIT(1)),
    Column('chipset', Text)
)


class Product(Base):
    __tablename__ = 'product'

    ProductID = Column(Integer, primary_key=True)
    description = Column(Text)
    imagePath = Column(Text)
    name = Column(String(255), nullable=False, unique=True)


class ProductRetailer(Base):
    __tablename__ = 'product_retailer'

    ProductID = Column(ForeignKey('product.ProductID'), primary_key=True, nullable=False, index=True)
    RetailerID = Column(ForeignKey('retailer.RetailerID'), primary_key=True, nullable=False, index=True)
    url = Column(Text)
    price = Column(Numeric(10, 2), nullable=False)

    product = relationship('Product')
    retailer = relationship('Retailer')


class Pro(Base):
    __tablename__ = 'pros'

    ReviewID = Column(ForeignKey('review.ReviewID'), nullable=False, index=True)
    ID = Column(Integer, primary_key=True)
    fact = Column(Text, nullable=False)

    review = relationship('Review')


t_psu = Table(
    'psu', metadata,
    Column('ProductID', ForeignKey('product.ProductID'), nullable=False, index=True),
    Column('power', Text),
    Column('formFactor', Text),
    Column('modular', BIT(1)),
    Column('width', Text),
    Column('depth', Text),
    Column('height', Text),
    Column('weight', Text),
    Column('brand', Text)
)


t_ram = Table(
    'ram', metadata,
    Column('ProductID', ForeignKey('product.ProductID'), nullable=False, index=True),
    Column('capacity', Text),
    Column('technology', Text),
    Column('formFactor', Text),
    Column('speed', Text),
    Column('casLatens', Text),
    Column('type', Text)
)


class Retailer(Base):
    __tablename__ = 'retailer'

    RetailerID = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False, unique=True)


class Review(Base):
    __tablename__ = 'review'

    ReviewID = Column(Integer, primary_key=True)
    reviewDate = Column(Date, nullable=False)
    crawlDate = Column(Date, nullable=False)
    content = Column(String, nullable=False)
    productRating = Column(Float)
    reviewRating = Column(Float)
    author = Column(String(255))
    positiveCount = Column(Integer)
    negativeCount = Column(Integer)
    verifiedPurchase = Column(BIT(1))
    isCriticReview = Column(BIT(1), nullable=False)
    productType = Column(String(255), nullable=False)
    url = Column(String(255), nullable=False, unique=True)
    title = Column(Text, nullable=False)
    maxRating = Column(Float)


class Reviewcomment(Base):
    __tablename__ = 'reviewcomment'

    ReviewID = Column(ForeignKey('review.ReviewID'), nullable=False, index=True)
    ID = Column(Integer, primary_key=True)
    content = Column(Text)
    rating = Column(Float)

    review = relationship('Review')
